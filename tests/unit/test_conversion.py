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

        if __name__ == '__main__':
            unittest.main()
