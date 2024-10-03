from configparser import ConfigParser
from typing import Optional

from pystratum_backend.Backend import Backend
from pystratum_backend.RoutineLoaderWorker import RoutineLoaderWorker
from pystratum_backend.RoutineWrapperGeneratorWorker import RoutineWrapperGeneratorWorker
from pystratum_backend.StratumIO import StratumIO

from pystratum_sqlite.backend.SqliteRoutineLoaderWorker import SqliteRoutineLoaderWorker
from pystratum_sqlite.backend.SqliteRoutineWrapperGeneratorWorker import SqliteRoutineWrapperGeneratorWorker


class SqliteBackend(Backend):
    """
    PyStratum Backend for SQLite.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def create_routine_loader_worker(self, config: ConfigParser, io: StratumIO) -> Optional[RoutineLoaderWorker]:
        """
        Creates the object that does the actual execution of the routine loader command for the backend.

        :param config: The settings from the PyStratum configuration file.
        :param io: The output object.
        """
        return SqliteRoutineLoaderWorker(io, config)

    # ------------------------------------------------------------------------------------------------------------------
    def create_routine_wrapper_generator_worker(self, config: ConfigParser, io: StratumIO) \
            -> Optional[RoutineWrapperGeneratorWorker]:
        """
        Creates the object that does the actual execution of the routine wrapper generator command for the backend.

        :param config: The settings from the PyStratum configuration file.
        :param io: The output object.
        """
        return SqliteRoutineWrapperGeneratorWorker(io, config)

# ----------------------------------------------------------------------------------------------------------------------
