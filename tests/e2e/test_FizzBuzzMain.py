import unittest
from typing import Any

import approvaltests
from approvaltests.reporters import PythonNativeReporter

from tests.approval_tests.command_helper import CommandHelper


class TestFizzBuzzMain(unittest.TestCase):
    command_helper: CommandHelper
    approvaltests.set_default_reporter(PythonNativeReporter())

    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.command_helper = CommandHelper()

    def setUp(self) -> None:
        # approvaltests.set_default_reporter(())
        pass

    def test_top_level_execution(self) -> None:
        approvaltests.verify(self.command_helper.invoke_command(
            self.command_helper.to_list("""\
python3 ./main.py
""")))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
