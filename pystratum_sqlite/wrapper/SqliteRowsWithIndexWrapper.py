from pystratum_common.wrapper.CommonRowsWithIndexWrapper import CommonRowsWithIndexWrapper
from pystratum_common.wrapper.helper.WrapperContext import WrapperContext

from pystratum_sqlite.wrapper.helper.SqlHelper import SqlHelper


class SqliteRowsWithIndexWrapper(CommonRowsWithIndexWrapper):
    """
    Wrapper method generator for stored procedures whose result set must be returned using tree structure using a
    combination of non-unique columns.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_execute_rows(self, context: WrapperContext) -> None:
        """
        Builds the code for invoking the stored routine.

        :param context: The loader context.
        """
        if len(context.pystratum_metadata['parameters']) > 0:
            params = list(
                    map(lambda item: f"'{item['name']}': {item['name']}", context.pystratum_metadata['parameters']))
            context.code_store.append_line(f"params = {{{', '.join(params)}}}")
        else:
            context.code_store.append_line("params = {}")

        parts = SqlHelper.split(context.pystratum_metadata['source'])

        for index in range(len(parts) - 1):
            context.code_store.append_line(f"query = '\\n' * {parts[index][0] + context.pystratum_metadata['offset']}")
            context.code_store.append_line(f'query += """{parts[index][1]}"""')
            context.code_store.append_line(f'self.execute_none(query, params)')
            context.code_store.append_line()

        context.code_store.append_line(f"query = '\\n' * {parts[-1][0] + context.pystratum_metadata['offset']}")
        context.code_store.append_line(f'query += """{parts[-1][1]}"""')
        context.code_store.append_line('rows = self.execute_rows(query, params)')

# ----------------------------------------------------------------------------------------------------------------------
