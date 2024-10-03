from pystratum_common.wrapper.helper import WrapperContext

from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper


class SqliteLastInsertRowIdWrapper(SqliteWrapper):
    """
    Wrapper method generator for a stored procedure that inserts rows in a table with an auto increment key.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _return_type_hint(self, context: WrapperContext) -> str:
        """
        Returns the return type of the wrapper method.

        :param context: The build context.
        """
        return 'int'

    # ------------------------------------------------------------------------------------------------------------------
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        return 'execute_last_insert_id'

# ----------------------------------------------------------------------------------------------------------------------
