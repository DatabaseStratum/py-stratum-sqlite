from pystratum_common.wrapper.CommonWrapper import CommonWrapper
from pystratum_common.wrapper.helper import WrapperContext

from pystratum_sqlite.wrapper.SqliteBulkWrapper import SqliteBulkWrapper
from pystratum_sqlite.wrapper.SqliteLastInsertRowIdWrapper import SqliteLastInsertRowIdWrapper
from pystratum_sqlite.wrapper.SqliteNoneWrapper import SqliteNoneWrapper
from pystratum_sqlite.wrapper.SqliteRow0Wrapper import SqliteRow0Wrapper
from pystratum_sqlite.wrapper.SqliteRow1Wrapper import SqliteRow1Wrapper
from pystratum_sqlite.wrapper.SqliteRowsWithIndexWrapper import SqliteRowsWithIndexWrapper
from pystratum_sqlite.wrapper.SqliteRowsWithKeyWrapper import SqliteRowsWithKeyWrapper
from pystratum_sqlite.wrapper.SqliteRowsWrapper import SqliteRowsWrapper
from pystratum_sqlite.wrapper.SqliteSingleton0Wrapper import SqliteSingleton0Wrapper
from pystratum_sqlite.wrapper.SqliteSingleton1Wrapper import SqliteSingleton1Wrapper
from pystratum_sqlite.wrapper.SqliteWrapper import SqliteWrapper
from pystratum_sqlite.wrapper.SqliteYieldWrapper import SqliteYieldWrapper


def create_routine_wrapper(context: WrapperContext) -> CommonWrapper:
    """
    A factory for creating the appropriate object for generating a wrapper method for a stored context.stored_routine.

    :param context: The build context.

    :rtype: SqliteWrapper
    """
    designation_type = context.pystratum_metadata['designation']['type']

    if designation_type == 'bulk':
        wrapper = SqliteBulkWrapper()
    elif designation_type == 'last_insert_id':
        wrapper = SqliteLastInsertRowIdWrapper()
    elif designation_type == 'none':
        wrapper = SqliteNoneWrapper()
    elif designation_type == 'row0':
        wrapper = SqliteRow0Wrapper()
    elif designation_type == 'row1':
        wrapper = SqliteRow1Wrapper()
    elif designation_type == 'rows':
        wrapper = SqliteRowsWrapper()
    elif designation_type == 'rows_with_index':
        wrapper = SqliteRowsWithIndexWrapper()
    elif designation_type == 'rows_with_key':
        wrapper = SqliteRowsWithKeyWrapper()
    elif designation_type == 'singleton0':
        wrapper = SqliteSingleton0Wrapper()
    elif designation_type == 'singleton1':
        wrapper = SqliteSingleton1Wrapper()
    elif designation_type == 'yield':
        wrapper = SqliteYieldWrapper()
    else:
        raise Exception("Unknown stored routine type '{}'.".format(designation_type))

    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
