import dataclasses

import pytest

import typing as tp
import random, string

from .random_ds import RandomDS

def _generate_words(n: int) -> tp.Set[str]:

    words: tp.Set[str] = set()

    while len(words) != n:
        word_len = random.choice(range(3, 6))
        words.add("".join(random.choices(string.ascii_letters, k=word_len)))

    return words

@dataclasses.dataclass
class CaseWithoutRandom:
    methods: tp.List[tp.Any]
    values: tp.List[str]
    results: tp.List[bool]

TEST_CASES = [
    CaseWithoutRandom(
        methods=[RandomDS.add, RandomDS.erase, RandomDS.add, RandomDS.add],
        values=["a", "b", "a", "b"], 
        results=[True, False, False, True]),
    CaseWithoutRandom(
        methods=[RandomDS.erase, RandomDS.add, RandomDS.add, RandomDS.add],
        values=["a", "a", "b", "c"], 
        results=[False, True, True, True]),
    CaseWithoutRandom(
        methods=[RandomDS.add, RandomDS.erase, RandomDS.check, RandomDS.add, RandomDS.check],
        values=["a", "a", "a", "a", "a"], 
        results=[True, True, False, True, True]),
    CaseWithoutRandom(
        methods=[RandomDS.add, RandomDS.add, RandomDS.check],
        values=["a", "a", "a"], 
        results=[True, False, True]),    
    CaseWithoutRandom(
        methods=[RandomDS.add, RandomDS.add, RandomDS.add, RandomDS.add, RandomDS.erase, RandomDS.erase, RandomDS.erase, RandomDS.erase],
        values=["a", "b", "c", "d", "d", "c", "c", "a"], 
        results=[True, True, True, True, True, True, False, True]),
    CaseWithoutRandom(
        methods=[RandomDS.check, RandomDS.erase, RandomDS.add],
        values=["a", "a", "a"], 
        results=[False, False, True]),
]

@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_without_random(t: CaseWithoutRandom) -> None:
    rd = RandomDS()
    for i, method in enumerate(t.methods):
        assert method(rd, t.values[i]) == t.results[i]
 
def test_simple_random_empty() -> None:
    rd = RandomDS()
    assert rd.get_random() == ""

def test_simple_random_first() -> None:
    rd = RandomDS()
    rd.add("a")
    rd.add("b")
    rd.erase("a")
    for _ in range(10):
        assert rd.get_random() == "b"

def test_simple_random_second() -> None:
    rd = RandomDS()
    rd.add("a")
    rd.add("b")
    rd.add("c")
    rd.add("d")
    rd.add("e")
    rd.erase("c")
    rd.erase("a")
    rd.erase("d")
    rd.erase("e")
    rd.erase("b")
    rd.add("f")
    for _ in range(10):
        assert rd.get_random() == "f"

def test_big_random() -> None:
    rd = RandomDS()
    words = _generate_words(1000)
    list_words = list(words)
    for word in words:
        rd.add(word)
    random.shuffle(list_words)
    for i in range(500):
        words.discard(list_words[i])
        rd.erase(list_words[i])
    
    for _ in range(500):
        out_string = rd.get_random()
        assert out_string in words

def bench_function(obj, words):
    for word in words:
        obj.add(word)
    for word in words:
        obj.erase(word)
    for word in words:
        obj.add(word)
    for word in words:
        obj.erase(word)
        obj.get_random()

number_of_words = 100000

@pytest.mark.benchmark(group="User implementation", disable_gc=True, warmup=True, warmup_iterations=10)
def test_user_implementation(benchmark):
    words = _generate_words(number_of_words)
    benchmark.pedantic(bench_function, kwargs = {'obj': RandomDS(), 'words': words}, iterations=10, rounds=5)
