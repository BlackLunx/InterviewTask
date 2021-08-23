import typing as tp
import random


class RandomDS():

    def __init__(self):
        self._arr = []
        self._table = {}

    def add(self, string: str) -> bool:
        """
        :param string: The string to add to the data structure.
        :return: Information about the status of adding an object.
        """
        if string in self._table:
            return False
        size = len(self._arr)
        self._arr.append(string)
        self._table[string] = size
        return self.check(string)

    def erase(self, string: str) -> bool:
        """
        :param string: The string to erase from the data structure.
        :return: Information about the status of erasing an object.
        """
        idx = self._table.get(string, None)
        if idx is None:
            return False

        del self._table[string]
        size = len(self._arr)
        last = self._arr[size - 1]
        self._arr[idx], self._arr[size - 1] = self._arr[size - 1], self._arr[idx]
        del self._arr[-1]
        if self._table and string != last:
            self._table[last] = idx
        return not self.check(string)

    def get_random(self) -> str:
        """
        :return: Random string from data structure.
        """
        if not self._arr:
            return ""
        return random.choice(self._arr)

    def check(self, string: str) -> bool:
        """
        :param string: String to check for presence in the data structure
        :return: Information about an object.
        """
        slot = self._table.get(string, None)
        return slot is not None

    def size(self) -> int:
        """
        :return: Number of strings in data structure.
        """
        return len(self._arr)
