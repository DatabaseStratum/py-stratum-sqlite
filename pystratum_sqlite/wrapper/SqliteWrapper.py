import abc
from abc import ABC

from pystratum_common.wrapper.CommonWrapper import CommonWrapper
from pystratum_common.wrapper.helper import WrapperContext

from pystratum_sqlite.wrapper.helper.SqlHelper import SqlHelper


class SqliteWrapper(CommonWrapper, ABC):
    """
    Parent class for wrapper method generators for stored procedures and functions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _build_result_handler(self, context: WrapperContext) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
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
            self._build_method_invocation(context, 'execute_none', False)
            context.code_store.append_line()

        context.code_store.append_line(f"query = '\\n' * {parts[-1][0] + context.pystratum_metadata['offset']}")
        context.code_store.append_line(f'query += """{parts[-1][1]}"""')

        method = self._get_method()
        self._build_method_invocation(context, method, True)

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def _get_method(self) -> str:
        """
        Returns the method name of SqliteDataLayer for invoking the stored routine.
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def _build_method_invocation(self, context: WrapperContext, method: str, is_return: bool) -> None:
        """
        Builds the code for calling the stored routine in the wrapper method.

        :param context: The build context.
        :param method: The name of the method of SqliteDataLayer for invoking the stored routine.
        :param is_return: Whether the method should be returned.
        """
        text = 'return ' if is_return else ''

        if method == 'execute_bulk':
            return context.code_store.append_line(f'{text}self.{method}(bulk_handler, query, params)')

        return context.code_store.append_line(f'{text}self.{method}(query, params)')

# ----------------------------------------------------------------------------------------------------------------------
