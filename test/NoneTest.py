from test.StratumTestCase import StratumTestCase


class NoneTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test_number_of_affected_rows(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        self._dl.execute_none('drop table if exists TMP_TMP')
        self._dl.execute_none('create table TMP_TMP( c bigint )')
        ret = self._dl.execute_none('insert into TMP_TMP( c ) values(1)')
        self.assertEqual(1, ret, 'insert 1 row')
        ret = self._dl.execute_none('insert into TMP_TMP( c ) values(2), (3)')
        self.assertEqual(2, ret, 'insert 2 rows')
        ret = self._dl.execute_none('delete from TMP_TMP')
        self.assertEqual(3, ret, 'delete 3 rows')

# ----------------------------------------------------------------------------------------------------------------------
