from pystratum_common.wrapper.CommonRow0Wrapper import CommonRow0Wrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteRow0Wrapper(CommonRow0Wrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures that are selecting zero or one row.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_row0'

# ----------------------------------------------------------------------------------------------------------------------
