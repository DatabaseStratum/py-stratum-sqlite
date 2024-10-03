from pystratum_common.wrapper.CommonRow1Wrapper import CommonRow1Wrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteRow1Wrapper(CommonRow1Wrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures that are selecting one row.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_row1'

# ----------------------------------------------------------------------------------------------------------------------
