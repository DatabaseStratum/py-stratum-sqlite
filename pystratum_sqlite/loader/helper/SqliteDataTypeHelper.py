from typing import Any, Dict, List

from pystratum_common.loader.helper.CommonDataTypeHelper import CommonDataTypeHelper


class SqliteDataTypeHelper(CommonDataTypeHelper):
    """
    Utility class for deriving information based on an SQLite data type.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def all_column_types(self) -> List[str]:
        """
        Returns all column types supported by SQLite.
        """
        return ['int',
                'integer',
                'bool',
                'real',
                'text',
                'blob']

    # ------------------------------------------------------------------------------------------------------------------
    def column_type_to_python_type(self, data_type_info: Dict[str, Any]) -> str:
        """
        Returns the corresponding Python data type of SQLite data type.

        :param data_type_info: The SQLite data type metadata.
        """
        if data_type_info['data_type'] in ['bool', 'boolean']:
            return 'bool'

        if data_type_info['data_type'] in ['int', 'integer']:
            return 'int'

        if data_type_info['data_type'] == 'real':
            return 'float'

        if data_type_info['data_type'] == 'text':
            return 'str'

        if data_type_info['data_type'] == 'blob':
            return 'bytes'

        raise RuntimeError('Unknown data type {}.'.format(data_type_info['data_type']))

# ----------------------------------------------------------------------------------------------------------------------
