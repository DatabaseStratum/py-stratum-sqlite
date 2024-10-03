from configparser import ConfigParser
from typing import Any, Dict, List

from pystratum_backend.StratumIO import StratumIO
from pystratum_common.backend.CommonRoutineLoaderWorker import CommonRoutineLoaderWorker
from pystratum_common.loader.helper.LoaderContext import LoaderContext

from pystratum_sqlite.backend.SqliteWorker import SqliteWorker
from pystratum_sqlite.loader.SqliteRoutineLoader import SqliteRoutineLoader


class SqliteRoutineLoaderWorker(SqliteWorker, CommonRoutineLoaderWorker):
    """
    Class for mimicking loading stored routines into an SQLite instance from pseudo SQL files.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: StratumIO, config: ConfigParser):
        """
        Object constructor.

        :param io: The output decorator.
        """
        SqliteWorker.__init__(self, io, config)
        CommonRoutineLoaderWorker.__init__(self, io, config)

    # ------------------------------------------------------------------------------------------------------------------
    def _connect(self) -> None:
        """
        Connects to the database.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def _disconnect(self) -> None:
        """
        Disconnects from the database.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def _fetch_column_types(self) -> None:
        """
        Selects schema, table, column names and the column type from MySQL and saves them as replace pairs.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def _create_routine_loader(self, context: LoaderContext) -> SqliteRoutineLoader:
        """
        Creates a Routine Loader object.

        :param context: The loader context.
        """
        context.doc_block.param_tags_have_types = True

        return SqliteRoutineLoader(self._io)

    # ------------------------------------------------------------------------------------------------------------------
    def _fetch_rdbms_metadata(self) -> List[Dict[str, Any]]:
        """
        Retrieves information about all stored routines in the current schema.
        """
        return []

    # ------------------------------------------------------------------------------------------------------------------
    def _init_rdbms_specific(self) -> None:
        """
        Gets the SQL mode in the order as preferred by MySQL.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def _drop_stored_routine(self, rdbms_metadata: Dict[str, Any]) -> None:
        """
        Drops a stored routine.

        :param rdbms_metadata: The metadata from the RDBMS of the stored routine to be dropped.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _pystratum_metadata_revision() -> str:
        """
        Returns the revision of the format of the metadata of the stored routines.
        """
        return CommonRoutineLoaderWorker._pystratum_metadata_revision() + '.1'

# ----------------------------------------------------------------------------------------------------------------------
