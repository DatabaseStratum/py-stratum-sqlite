from pystratum_common.wrapper.CommonRowsWrapper import CommonRowsWrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteRowsWrapper(CommonRowsWrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures that are selecting zero, one, or more rows.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_rows'

# ----------------------------------------------------------------------------------------------------------------------
