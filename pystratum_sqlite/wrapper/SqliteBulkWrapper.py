from pystratum_common.wrapper.CommonBulkWrapper import CommonBulkWrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteBulkWrapper(CommonBulkWrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures with large result sets.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_bulk'

# ----------------------------------------------------------------------------------------------------------------------
