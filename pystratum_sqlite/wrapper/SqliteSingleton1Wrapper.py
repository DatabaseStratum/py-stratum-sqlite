from pystratum_common.wrapper.CommonSingleton1Wrapper import CommonSingleton1Wrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteSingleton1Wrapper(CommonSingleton1Wrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures that are selecting one row with one column only.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_singleton1'

# ----------------------------------------------------------------------------------------------------------------------
