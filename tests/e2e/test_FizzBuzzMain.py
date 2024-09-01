import unittest
from typing import Any

from tests.approval_tests.command_helper import CommandHelper
import approvaltests
from approvaltests.reporters import PythonNativeReporter

class TestFizzBuzzMain(unittest.TestCase):
    command_helper: CommandHelper
    approvaltests.set_default_reporter(PythonNativeReporter())

    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.command_helper = CommandHelper()

    def setUp(self) -> None:
        approvaltests.set_default_reporter(PythonNativeReporter())
        pass

    def test_(self) -> None:
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
