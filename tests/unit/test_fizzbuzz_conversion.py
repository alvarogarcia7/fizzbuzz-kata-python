import unittest
from typing import Any

import approvaltests
from approvaltests.reporters import ReportWithVSCodeMacOS

from tests.approval_tests.command_helper import CommandHelper


class FizzBuzz:
    def convert(self, number: int) -> str:
        if number % 15 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return str(number)


class TestFizzBuzzConversion(unittest.TestCase):
    command_helper: CommandHelper

    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.command_helper = CommandHelper()
        approvaltests.set_default_reporter(ReportWithVSCodeMacOS())

    def test_convert(self) -> None:
        approvaltests.verify_all("number to string", list(map(lambda x: str(x), range(1, 101))),
                                 lambda x: f"{x} => {FizzBuzz().convert(int(x))}")

        if __name__ == '__main__':
            unittest.main()
