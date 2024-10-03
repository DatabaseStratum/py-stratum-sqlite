from configparser import ConfigParser

from pystratum_backend.StratumIO import StratumIO


class SqliteWorker:
    """
    Parent class for commands which needs to connect to an SQLite database.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: StratumIO, config: ConfigParser):
        """
        Object constructor.

        :param io: The output decorator.
        """

        self._io: StratumIO = io
        """
        The output decorator.
        """

        self._config: ConfigParser = config
        """
        The configuration object.
        """

# ----------------------------------------------------------------------------------------------------------------------
