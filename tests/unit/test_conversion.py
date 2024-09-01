import re
import unittest
from typing import Any

import approvaltests
from approvaltests.reporters import ReportWithVSCodeMacOS

from fizzbuzz.conversion import FizzBuzz
from tests.approval_tests.command_helper import CommandHelper


class TestConversion(unittest.TestCase):
    command_helper: CommandHelper

    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.command_helper = CommandHelper()
        approvaltests.set_default_reporter(ReportWithVSCodeMacOS())

    def test_convert(self) -> None:
        approvaltests.verify_all("number to string", list(map(lambda x: str(x), range(1, 1000 + 1))),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_three_but_not_multiples_of_three(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '3' in str(i) and i % 3 != 0]
        self.verify_all(self.convert_list(subset), re.compile(r'^.*Fizz.*$'))
        approvaltests.verify_all("number to string: contains 3 but not multiple of 3",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_five_but_not_multiples_of_five(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '5' in str(i) and i % 5 != 0]
        self.verify_all(self.convert_list(subset), re.compile(r'^.*Buzz.*$'))
        approvaltests.verify_all("number to string: contains 5 but not multiple of 5",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_three_and_five_but_not_multiples_of_three_or_five(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '5' in str(i) and '3' in str(i) \
                             and not (i % 3 == 0 or i % 5 == 0)]
        self.verify_all(self.convert_list(subset), re.compile(r'FizzBuzz\d+'))

        approvaltests.verify_all("number to string: contains 3 and 5 but not (multiple of 3 or 5)",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_three_but_not_multiples_of_three_or_five(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '3' in str(i) and '5' not in str(i) \
                             and not (i % 3 == 0 or i % 5 == 0)]
        self.verify_all(self.convert_list(subset), re.compile(r'Fizz\d+'))

        approvaltests.verify_all("number to string: contains 3 but not (multiple of 3 or 5)",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_five_but_not_multiples_of_three_or_five(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '3' not in str(i) and '5' in str(i) \
                             and not (i % 3 == 0 or i % 5 == 0)]
        self.verify_all(self.convert_list(subset), re.compile(r'Buzz\d+'))

        approvaltests.verify_all("number to string: contains 3 but not (multiple of 3 or 5)",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_three_and_five_and_multiples_of_three_and_five(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '5' in str(i) and '3' in str(i) and i % 15 == 0]
        self.verify_all(self.convert_list(subset), re.compile(r'^FizzBuzzFizzBuzz$'))
        approvaltests.verify_all("number to string: contains 3 and 5 and multiple of 15",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    @staticmethod
    def verify_all(conversion_table: dict[int, str], regex: re.Pattern[str]) -> None:
        for number, converted in conversion_table.items():
            # Keep the variable in place. Otherwise, the assert message will not show the actual value. Intuition: regex.match cannot be represented as a string?
            none = regex.match(converted) is not None
            assert none, f"[number={number}] Expected '{converted}' to match '{regex.pattern}'"

    @staticmethod
    def convert_list(subset: list[int]) -> dict[int, str]:
        result: dict[int, str] = {number: FizzBuzz().convert(number) for number in subset}
        return result


if __name__ == '__main__':
    unittest.main()
