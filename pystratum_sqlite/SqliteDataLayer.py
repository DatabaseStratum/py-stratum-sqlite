import os.path
import re
import sqlite3
from pathlib import Path
from typing import Any, Dict, List

from pystratum_middle.BulkHandler import BulkHandler
from pystratum_middle.exception.ResultException import ResultException


class SqliteDataLayer:
    """
    Class for connecting to an SQLite instance and executing SQL statements. Also, a parent class for classes with
    static wrapper methods for executing stored procedures and functions.
    """

    yield_size: int = 10000
    """
    The number of rows to fetch for stored routines with designation type 'yield'.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, db: str | None = None, script: str | None = None, volatile: bool = False):
        """
        Object constructor.
        """

        self._db: sqlite3.Connection | None = None
        """
        The connection between Python and the SQLite instance.
        """

        self.line_buffered: bool = True
        """
        If True log messages from stored procedures with designation type 'log' are line buffered (Note: In python
        sys.stdout is buffered by default).
        """

        self.__last_sql: str = ''
        """
        The last executed SQL statement.
        """

        self.__path: str | None = None
        """
        The path to the SQLite database.
        """

        self.__volatile: bool = False
        """
        Whether the database is volatile. That is, the database file will be deleted before opening and closing the
        database.
        """

        self.__connect(db, script, volatile)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _dict_factory(cursor, row):
        ret = {}
        for idx, col in enumerate(cursor.description):
            ret[col[0]] = row[idx]

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def __connect_memory(self, script: str | None) -> None:
        """
        Creates a connection to an in memory SQLite instance.

        :param script:
        """
        self._db = sqlite3.connect(':memory:')

        if script is not None:
            self.__execute_script(script)

    # ------------------------------------------------------------------------------------------------------------------
    def __execute_script(self, script: str) -> None:
        """
        Executes

        :param script: The path to the script.
        """
        sql = Path(script).read_text()

        parts = re.split(r'(;)[ \t\f]*\n', sql)
        offset = 0
        for index, part in enumerate(parts):
            if index < len(parts) - 1 and parts[index + 1] == ';':
                sql = "\n" * offset
                sql += part

                self.execute_none(sql)

                offset += part.count("\n") + 1

    # ------------------------------------------------------------------------------------------------------------------
    def __connect_file(self, db: str, script: str | None, volatile: bool) -> None:
        """
        Creates a connection to an SQLite instance.
        """
        exists = os.path.isfile(db)
        if volatile and exists:
            os.unlink(db)

        self._db = sqlite3.connect(f'sqlite:{db}')
        self.__path = os.path.realpath(db)
        self.__volatile = volatile

        if script is not None and (volatile or exists):
            self.__execute_script(script)

    # ------------------------------------------------------------------------------------------------------------------
    def __connect(self, db: str | None, script: str | None, volatile: bool) -> None:
        """
        Creates a connection to an SQLite instance.
        """
        if db is None:
            self.__connect_memory(script)

        elif isinstance(script, str):
            self.__connect_file(db, script, volatile)

        else:
            ValueError(f'A {db.__class__} is not a valid argument for db')

    # ------------------------------------------------------------------------------------------------------------------
    def commit(self) -> None:
        """
        Commits the current transaction.
        See https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html
        """
        self._db.commit()

    # ------------------------------------------------------------------------------------------------------------------
    def execute_bulk(self, bulk_handler: BulkHandler, sql: str, params: Dict | None = None) -> int:
        """
        Executes a stored routine with designation type "bulk". Returns the number of rows processed.

        :param bulk_handler: The bulk handler for processing the selected rows.
        :param sql: The SQL statement for calling the stored routine.
        :param params: The arguments for calling the stored routine.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = self._dict_factory
        itr = cursor.execute(sql, params)
        bulk_handler.start()

        rowcount = 0
        for row in itr:
            rowcount += 1
            bulk_handler.row(row)

        cursor.close()
        bulk_handler.stop()

        return rowcount

    # ------------------------------------------------------------------------------------------------------------------
    def execute_none(self, sql: str, params: Dict | None = None) -> int:
        """
        Executes a query that does not select any rows. Returns the number of affected rows.

        :param sql: The SQL statement.
        :param params: The values for the statement.
        """
        self.__last_sql = sql

        if params is None:
            params = {}

        cursor = self._db.cursor()
        cursor.row_factory = None
        cursor.execute(sql, params)
        rowcount = cursor.rowcount
        cursor.close()

        return rowcount

    # ------------------------------------------------------------------------------------------------------------------
    def execute_last_insert_id(self, sql: str, params: Dict | None = None) -> int:
        """
        Executes a query that inserts rows in a table with an auto increment key.

        :param sql: The SQL statement.
        :param params: The values for the statement.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = None
        cursor.execute(sql, params)
        last_row_id = cursor.lastrowid
        cursor.close()

        return last_row_id

    # ------------------------------------------------------------------------------------------------------------------
    def execute_row0(self, sql: str, params: Dict | None = None) -> Dict[str, Any] | None:
        """
        Executes a stored procedure that selects zero or one row. Returns the selected row or None.

        :param sql: The SQL code to execute the stored procedure.
        :param params: The arguments for the stored procedure.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = self._dict_factory
        itr = cursor.execute(sql, params)
        rows = itr.fetchall()
        rowcount = len(rows)
        if rowcount == 1:
            ret = rows[0]
        else:
            ret = None  # Keep our IDE happy.
        cursor.close()

        if not (rowcount == 0 or rowcount == 1):
            raise ResultException('0 or 1', rowcount, sql)

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def execute_row1(self, sql: str, params: Dict | None = None) -> Dict[str, Any]:
        """
        Executes a stored procedure that selects one row. Returns the selected row.

        :param sql: The SQL code to execute the stored procedure.
        :param params: The arguments for the stored procedure.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = self._dict_factory
        itr = cursor.execute(sql, params)
        rows = itr.fetchall()
        rowcount = len(rows)
        if rowcount == 1:
            row = rows[0]
        else:
            row = None  # Keep our IDE happy.
        cursor.close()

        if rowcount != 1:
            raise ResultException('1', rowcount, sql)

        return row

    # ------------------------------------------------------------------------------------------------------------------
    def execute_rows(self, sql: str, params: Dict | None = None) -> List[Dict[str, Any]]:
        """
        Executes a stored procedure that selects zero or more rows. Returns the selected rows (an empty list if no rows
        are selected).

        :param sql: The SQL code to execute the stored procedure.
        :param params: The arguments for the statement.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = self._dict_factory
        itr = cursor.execute(sql, params)
        rows = itr.fetchall()
        cursor.close()

        return rows

    # ------------------------------------------------------------------------------------------------------------------
    def execute_singleton0(self, sql: str, params: Dict | None = None) -> Any:
        """
        Executes a stored procedure that selects zero or one row with one column. Returns the value of selected column
        or None.

        :param sql: The SQL code to execute the stored procedure.
        :param params: The arguments for the stored procedure.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = None
        itr = cursor.execute(sql, params)
        rows = itr.fetchall()
        rowcount = len(rows)
        if rowcount == 1:
            ret = rows[0][0]
        else:
            ret = None  # Keep our IDE happy.
        cursor.close()

        if not (rowcount == 0 or rowcount == 1):
            raise ResultException('0 or 1', rowcount, sql)

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def execute_singleton1(self, sql: str, params: Dict | None = None) -> Any:
        """
        Executes a stored routine with designation type "singleton1", i.e., a stored routine expected to select one row
        with one column.

        :param sql: The SQL code to execute the stored procedure.
        :param params: The arguments for the stored procedure.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = None
        itr = cursor.execute(sql, params)
        rows = itr.fetchall()
        rowcount = len(rows)
        if rowcount == 1:
            ret = rows[0][0]
        else:
            ret = None  # Keep our IDE happy.
        cursor.close()

        if rowcount != 1:
            raise ResultException('1', rowcount, sql)

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def execute_yield(self, sql: str, params: Dict | None = None):
        """
        Executes a stored procedure that selects zero or more rows. The

        :param sql: The SQL code to execute the stored procedure.
        :param params: The arguments for the statement.
        """
        self.__last_sql = sql

        cursor = self._db.cursor()
        cursor.row_factory = self._dict_factory
        itr = cursor.execute(sql, params)
        while True:
            rows = itr.fetchmany(SqliteDataLayer.yield_size)
            if not rows:
                cursor.close()
                return
            yield rows

    # ------------------------------------------------------------------------------------------------------------------
    def last_sql(self) -> str:
        """
        Returns the last execute SQL statement.
        """
        return self.__last_sql

    # ------------------------------------------------------------------------------------------------------------------
    def rollback(self) -> None:
        """
        Rolls back the current transaction.
        See https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-rollback.html
        """
        self._db.rollback()

# ----------------------------------------------------------------------------------------------------------------------
