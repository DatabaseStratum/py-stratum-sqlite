import unittest

from cleo.testers.command_tester import CommandTester
from pystratum_cli import StratumApplication


class AAATest(unittest.TestCase):
    """
    This test must run before all other tests because this test loads the stored routines.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Runs the stratum command: loads the stored routines and generates the stored routine wrapper.
        """
        application = StratumApplication()
        command = application.find('stratum')
        command_tester = CommandTester(command)
        status = command_tester.execute('test/etc/stratum.cfg')

        print(command_tester.io.fetch_output())

        self.assertEqual(0, status)

# ----------------------------------------------------------------------------------------------------------------------
