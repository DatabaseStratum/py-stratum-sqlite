from configparser import ConfigParser

from pystratum_backend.StratumIO import StratumIO
from pystratum_common.backend.CommonRoutineWrapperGeneratorWorker import CommonRoutineWrapperGeneratorWorker
from pystratum_common.wrapper.helper import WrapperContext

from pystratum_sqlite.backend.SqliteWorker import SqliteWorker
from pystratum_sqlite.wrapper import create_routine_wrapper


class SqliteRoutineWrapperGeneratorWorker(SqliteWorker, CommonRoutineWrapperGeneratorWorker):
    """
    Class for generating a class with wrapper methods for calling stored routines in an SQLite database.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: StratumIO, config: ConfigParser):
        """
        Object constructor.

        :param io: The output decorator.
        """
        SqliteWorker.__init__(self, io, config)
        CommonRoutineWrapperGeneratorWorker.__init__(self, io, config)

    # ------------------------------------------------------------------------------------------------------------------
    def _build_routine_wrapper(self, context: WrapperContext) -> None:
        """
        Builds a complete wrapper method for a stored routine.

        :param context: The build context.
        """
        wrapper = create_routine_wrapper(context)
        wrapper.build(context)

# ----------------------------------------------------------------------------------------------------------------------
