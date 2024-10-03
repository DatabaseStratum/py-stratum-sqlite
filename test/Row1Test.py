from pystratum_middle.exception.ResultException import ResultException

from test.StratumTestCase import StratumTestCase


class Row1Test(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type row1 must return 1 row and 1 row only.
        """
        ret = self._dl.tst_test_row1a(1)
        self.assertIsInstance(ret, dict)

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        """
        An exception must be thrown when a stored routine with designation type row1 returns 0 rows.
        @expectedException Exception
        """
        with self.assertRaises(ResultException):
            self._dl.tst_test_row1a(0)

    # ------------------------------------------------------------------------------------------------------------------
    def test3(self):
        """
        An exception must be thrown when a stored routine with designation type row1 returns more than 1 rows.
        @expectedException Exception
        """
        with self.assertRaises(ResultException):
            self._dl.tst_test_row1a(2)

# ----------------------------------------------------------------------------------------------------------------------
