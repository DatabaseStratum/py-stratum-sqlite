from pystratum_common.wrapper.CommonNoneWrapper import CommonNoneWrapper

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteNoneWrapper(CommonNoneWrapper, SqliteWrapper):
    """
    Wrapper method generator for stored procedures without any result set.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_none'

# ----------------------------------------------------------------------------------------------------------------------
