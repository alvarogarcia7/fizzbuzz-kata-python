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
        approvaltests.verify_all("number to string", list(map(lambda x: str(x), range(1, 101))),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_three_but_not_multiples_of_three(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '3' in str(i) and i % 3 != 0]
        converted = [FizzBuzz().convert(x) for x in subset]
        assert all('Fizz' in x for x in converted)
        approvaltests.verify_all("number to string: contains 3 but not multiple of 3",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

    def test_convert_contains_five_but_not_multiples_of_five(self) -> None:
        subset: list[int] = [i for i in range(1, 1000) if '5' in str(i) and i % 5 != 0]
        converted = [FizzBuzz().convert(x) for x in subset]
        assert all('Buzz' in x for x in converted)
        approvaltests.verify_all("number to string: contains 5 but not multiple of 5",
                                 list(map(lambda x: str(x), subset)),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")


if __name__ == '__main__':
    unittest.main()
