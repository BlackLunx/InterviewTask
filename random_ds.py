import typing as tp

class RandomDS():
    
    def add(self, string: str) -> bool:
        """
        :param string: The string to add to the data structure.
        :return: Information about the status of adding an object. 
        """
        return False

    def erase(self, string: str) -> bool:
        """
        :param string: The string to erase from the data structure.
        :return: Information about the status of erasing an object. 
        """
        return False

    def get_random(self) -> str:
        """
        :return: Random string from data structure. 
        """
        return ""

    def check(self, string: str) -> bool:
        """
        :param string: String to check for presence in the data structure
        :return: Information about an object. 
        """
        return False

    def size(self) -> int:
        """
        :return: Number of strings in data structure. 
        """
        return 0