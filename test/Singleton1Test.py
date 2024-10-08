from pystratum_middle.exception.ResultException import ResultException

from test.StratumTestCase import StratumTestCase


class Singleton1Test(StratumTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type singleton1 must return 1 value and 1 value only.
        """
        ret = self._dl.tst_test_singleton1a(1)
        self.assertEqual(1, ret)

    # ------------------------------------------------------------------------------------------------------------------
    def test2(self):
        """
        An exception must be thrown when a stored routine with designation type singleton1 returns 0 values.
        @expectedException Exception
        """
        with self.assertRaises(ResultException):
            self._dl.tst_test_singleton1a(0)

    # ------------------------------------------------------------------------------------------------------------------
    def test3(self):
        """
        An exception must be thrown when a stored routine with designation type singleton1 returns more than 1 value.
        @expectedException Exception
        """
        with self.assertRaises(ResultException):
            self._dl.tst_test_singleton1a(2)

# ----------------------------------------------------------------------------------------------------------------------
