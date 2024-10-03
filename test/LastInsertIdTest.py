from pystratum_sqlite.SqliteDataLayer import SqliteDataLayer
from test.StratumTestCase import StratumTestCase


class LastInsertIdTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Test stored routine with designation type last_insert_id.
        """
        row_id = self._dl.tst_test_last_insert_id('row1')
        self.assertEqual(1, row_id)

        row_id = self._dl.tst_test_last_insert_id('row2')
        self.assertEqual(2, row_id)

# ----------------------------------------------------------------------------------------------------------------------
