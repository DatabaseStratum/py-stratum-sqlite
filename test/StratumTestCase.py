import sys
import unittest
from io import StringIO

from test.TestDataLayer import TestDataLayer


class StratumTestCase(unittest.TestCase):
    def __init__(self, method_name):
        """
        Object constructor.
        """
        super().__init__(method_name)

        self._dl: TestDataLayer | None = None
        """
        The generated data layer.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def setUp(self):
        self._dl = TestDataLayer(script='test/ddl/0100_create_tables.sql')

        self.held, sys.stdout = sys.stdout, StringIO()

    # ------------------------------------------------------------------------------------------------------------------
    def tearDown(self):
        sys.stdout = self.held
        self._dl = None

# ----------------------------------------------------------------------------------------------------------------------
