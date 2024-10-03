import sys

from test.StratumTestCase import StratumTestCase
from test.TestBulkHandler import TestBulkHandler


class BulkTest(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        bulk_handler = TestBulkHandler()
        n = self._dl.tst_test_bulk(bulk_handler, 3)

        self.assertEqual(3, n)

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, 'start\n1\n2\n3\nstop')

# ----------------------------------------------------------------------------------------------------------------------
