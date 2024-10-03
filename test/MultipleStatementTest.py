from pystratum_middle.exception.ResultException import ResultException

from test.StratumTestCase import StratumTestCase


class MultipleStatementTest(StratumTestCase):
    """
    Test cases for stored routines with multiple statements
    """
    # ------------------------------------------------------------------------------------------------------------------
    def testLastStatement(self):
        """
        Stored routine with designation type singleton1 must return 1 value and 1 value only.
        """
        text = self._dl.tst_test_execute_leading_queries()
        self.assertEqual('Hello, world!', text)

# ----------------------------------------------------------------------------------------------------------------------
