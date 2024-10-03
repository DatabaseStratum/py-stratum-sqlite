from pystratum_common.wrapper.CommonRowsWrapper import CommonRowsWrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteYieldWrapper(CommonRowsWrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures that are selecting a large number of rows.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_yield'

# ----------------------------------------------------------------------------------------------------------------------
