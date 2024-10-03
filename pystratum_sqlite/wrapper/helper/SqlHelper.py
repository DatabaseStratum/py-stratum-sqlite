import re
from typing import List, Tuple


class SqlHelper:
    """
    Utility class for splitting an SQL script into multiple SQL statements.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def split(script: str) -> List[Tuple[int, str]]:
        """
        Splits a SQL script into multiple SQL statements.

        :param script: The SQL statements.
        """
        script_parts = re.split(r'(;)[ \t\f]*\n', script + '\n')
        if len(script_parts) > 1:
            offset = 0
            statements = []
            for index, script_part in enumerate(script_parts):
                if index < len(script_parts) - 1 and script_parts[index + 1] == ';':
                    query_parts = re.match(r'(?P<whitespace>[ \t\f\n]*)(?P<sql>[\S\n\t\v ]*)', script_part)
                    sql = query_parts['sql'].strip() + '\n'
                    statements.append((offset + query_parts['whitespace'].count('\n'), str(sql)))
                    offset += script_part.count('\n') + 1
        else:
            sql = script.rstrip()
            sql += '\n'
            statements = [(0, script)]

        return statements

# ----------------------------------------------------------------------------------------------------------------------
