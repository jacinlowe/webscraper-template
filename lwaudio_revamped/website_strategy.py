from abc import ABC, abstractmethod
from typing import Callable, Dict, List

from lwaudio_revamped.scraper import Scraper


class Website(ABC):
    def __init__(self, scraper: Scraper) -> None:
        self.scraper = scraper

    def export_fields(self) -> List[Callable]:
        """collects all the methods in the class except the exceptions. Prepares them to be ran in sequence"""
        method_list = [
            func
            for func in dir(self)
            if callable(getattr(self, func))
            and not func.startswith("__")
            and not func.startswith("_")
            and not func.startswith("export_fields")
            and not func.startswith("data")
            and not func.startswith("get_all_data")
        ]

        return method_list

    def get_all_data(self) -> Dict:
        """Runs all the methods in sequence then merges the output data into a dictionary"""
        data = {}
        for i in self.export_fields():
            class_method = getattr(self, i)
            result = class_method()
            data = data | result
        return data

    @abstractmethod
    def _template(self) -> dict:
        """Gives a good representation of how each function should work
        underscore will not run in the collector
        """
        try:
            pass
        except:
            pass

        return_data = {}
        return return_data


if __name__ == "__main__":

    class TestClass(Website):
        def func1(self):
            print(1)
            return {"test": 1}

        def func2(self):
            print(2)
            return {"tip": 2}

        def func3(self):
            print(3)
            return {"tips": 4}

    test = TestClass()
    test.get_all_data()
