from pystratum_common.wrapper.CommonSingleton0Wrapper import CommonSingleton0Wrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteSingleton0Wrapper(CommonSingleton0Wrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures that are selecting zero or one row with one column only.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_singleton0'

# ----------------------------------------------------------------------------------------------------------------------
