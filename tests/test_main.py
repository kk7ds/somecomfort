import unittest
import sys

import mock

from somecomfort import __main__ as main


class TestMain(unittest.TestCase):
    def test_main_simple(self):
        sys.stdout = sys.stderr = mock.MagicMock()
        try:
            main.main()
        except SystemExit:
            pass
