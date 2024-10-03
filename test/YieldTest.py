from pystratum_sqlite.SqliteDataLayer import SqliteDataLayer
from test.StratumTestCase import StratumTestCase


class YieldTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type yield
        """
        SqliteDataLayer.yield_size = 2
        count1 = 0
        count2 = 0
        for rows in self._dl.tst_test_yield(3):
            count1 += 1
            count2 += len(rows)

        self.assertEqual(2, count1)
        self.assertEqual(3, count2)

# ----------------------------------------------------------------------------------------------------------------------
