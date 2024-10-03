import re

from pystratum_backend.StratumIO import StratumIO
from pystratum_common.loader.CommonRoutineLoader import CommonRoutineLoader
from pystratum_common.loader.helper.CommonDataTypeHelper import CommonDataTypeHelper
from pystratum_common.loader.helper.LoaderContext import LoaderContext

from pystratum_sqlite.loader.helper.SqliteDataTypeHelper import SqliteDataTypeHelper
from pystratum_sqlite.SqliteDataLayer import SqliteDataLayer


class SqliteRoutineLoader(CommonRoutineLoader):
    """
    Class for loading a single stored routine into an SQLite instance from a (pseudo) SQL file.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: StratumIO):
        """
        Object constructor.

        :param io: The output decorator.
        """
        CommonRoutineLoader.__init__(self, io)

        self.__offset: int = 0
        """
        The offset of the first line of the payload of the stored routine ins the source file.
        """

        self.__dl: SqliteDataLayer = SqliteDataLayer()

    # ------------------------------------------------------------------------------------------------------------------
    def _get_data_type_helper(self) -> CommonDataTypeHelper:
        """
        Returns a data type helper object for Sqlite.
        """
        return SqliteDataTypeHelper()

    # ------------------------------------------------------------------------------------------------------------------
    def _extract_insert_many_table_columns(self, context: LoaderContext) -> None:
        """
        Extracts the column names and column types of the current table for bulk insert.

        :param context: The loader context.
        """
        if context.doc_block.designation['type'] == 'insert_many':
            raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def _extract_name(self, context: LoaderContext) -> None:
        """
        Extracts the name of the stored routine and the stored routine type (i.e., procedure or function) source.

        :param context: The loader context.
        """
        context.stored_routine.type = 'procedure'

    # ------------------------------------------------------------------------------------------------------------------
    def _extract_stored_routine_parameters(self, context: LoaderContext) -> None:
        """
        Extracts the metadata of the stored routine parameters.

        :param context: The loader context.
        """
        doc_block_parameters = context.doc_block.parameters()

        body = "\n".join(context.stored_routine.code_lines[self.__offset - 1:])
        matches = re.findall(r'(:[a-zA-Z_][a-zA-Z0-9_]*)', body)
        matches = list(match.lstrip(':') for match in matches)
        tmp_parameters = []
        for match in sorted(set(matches)):
            data_type = 'int'
            for doc_block_parameter in doc_block_parameters:
                if doc_block_parameter['name'] == match.lstrip(':'):
                    data_type = doc_block_parameter['type']
                    break
            tmp_parameters.append({'name':                 match.lstrip(':'),
                                   'data_type':            data_type,
                                   'data_type_descriptor': data_type})

        parameters = []
        for doc_block_parameter in doc_block_parameters:
            for index, tmp_parameter in enumerate(tmp_parameters):
                if doc_block_parameter['name'] == tmp_parameter['name']:
                    parameters.append(tmp_parameter)
                    tmp_parameters.pop(index)
        parameters += tmp_parameters

        context.stored_routine.parameters = parameters

    # ------------------------------------------------------------------------------------------------------------------
    def _load_routine_file(self, context: LoaderContext) -> None:
        """
        Mimics loading the stored routine into the database.

        :param context: The loader context.
        """
        self._io.text('Loading {0} <dbo>{1}</dbo>'.format(context.stored_routine.type, context.stored_routine.name))

        self.__offset = self.__get_offset(context)
        context.new_pystratum_metadata['offset'] = self.__offset
        context.new_pystratum_metadata['source'] = "\n".join(context.stored_routine.code_lines[self.__offset:])

    # ------------------------------------------------------------------------------------------------------------------
    def _drop_stored_routine(self, context: LoaderContext) -> None:
        """
        Drops the stored routine if it exists.

        :param context: The loader context.
        """
        pass  # Nothing to do.

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __get_offset(context: LoaderContext):
        """
        Find s the first line of code of the stored routine.

        :param context: The loader context.
        """
        line2 = None
        for index, line in enumerate(context.stored_routine.code_lines):
            if re.match(r'^\s*\*/\s*$', line):
                line2 = index
                break

        return line2 + 1

# ----------------------------------------------------------------------------------------------------------------------
