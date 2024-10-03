from pystratum_middle.BulkHandler import BulkHandler
from pystratum_sqlite.SqliteDataLayer import SqliteDataLayer
from typing import Any
from typing import Dict
from typing import List


class TestDataLayer(SqliteDataLayer):
    """
    The stored routines wrappers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tst_magic_constant05(self) -> str:
        """
        Test for magic constant.
        """
        params = {}
        query = '\n' * 5
        query += """select __DIR__
"""
        return self.execute_singleton1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_strtr(self, p1: int | None, p100: int | None, p10: int | None) -> Dict[str, Any]:
        """
        Test strtr does not mix up parameters with nearly same name.

        :param p1: Parameter of type int.
                   RDBMS data type: int
        :param p100: Parameter of type int.
                     RDBMS data type: int
        :param p10: Parameter of type int.
                    RDBMS data type: int
        """
        params = {'p1': p1, 'p100': p100, 'p10': p10}
        query = '\n' * 9
        query += """select :p1   as p1
,      :p100 as p100a
,      :p10  as p10
,      :p100 as p100b
"""
        return self.execute_row1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test01(self, p_tst_int: int | None, p_tst_real: float | None, p_tst_text: str | None, p_tst_blob: bytes | None) -> int:
        """
        Test for all possible types of parameters including BLOBs.

        :param p_tst_int: Parameter of type int.
                          RDBMS data type: int
        :param p_tst_real: Parameter of type real.
                           RDBMS data type: real
        :param p_tst_text: Parameter of type text.
                           RDBMS data type: text
        :param p_tst_blob: Parameter of type blob.
                           RDBMS data type: blob
        """
        params = {'p_tst_int': p_tst_int, 'p_tst_real': p_tst_real, 'p_tst_text': p_tst_text, 'p_tst_blob': p_tst_blob}
        query = '\n' * 10
        query += """insert into TST_FOO1( tst_int
,                     tst_real
,                     tst_text
,                     tst_blob )
values( :p_tst_int
,       :p_tst_real
,       :p_tst_text
,       :p_tst_blob )
"""
        return self.execute_none(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_bulk(self, bulk_handler: BulkHandler, p_count: int | None) -> int:
        """
        Test for designation type bulk.

        :param bulk_handler: The bulk handler for processing the selected rows.
        :param p_count: The number of rows selected.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 7
        query += """select *
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_bulk(bulk_handler, query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_execute_leading_queries(self) -> str:
        """
        Test comment add end is ignored.
        """
        params = {}
        query = '\n' * 5
        query += """create table TMP_FOO
(
    text varchar(100)
)
"""
        self.execute_none(query, params)

        query = '\n' * 10
        query += """create index TMP_IDX01 on TMP_FOO(text)
"""
        self.execute_none(query, params)

        query = '\n' * 12
        query += """insert into TMP_FOO(text)
values
    ('Hello, world!')
"""
        self.execute_none(query, params)

        query = '\n' * 16
        query += """select text
from TMP_FOO
"""
        return self.execute_singleton1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_illegal_query(self) -> List[Dict[str, Any]]:
        """
        Test for illegal query.
        """
        params = {}
        query = '\n' * 5
        query += """drop table if exists TST_FOOBAR
"""
        self.execute_none(query, params)

        query = '\n' * 7
        query += """drop table if exists TST_FOOBAR
"""
        self.execute_none(query, params)

        query = '\n' * 9
        query += """select * from NOT_EXISTS
"""
        return self.execute_rows(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_last_insert_id(self, p_tst_test: str | None) -> int:
        """
        Test case for designation type last_insert_id.

        :param p_tst_test: Some value.
                           RDBMS data type: text
        """
        params = {'p_tst_test': p_tst_test}
        query = '\n' * 7
        query += """insert into TST_LAST_INSERT_ID( tst_test )
values( :p_tst_test )
"""
        return self.execute_last_insert_id(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_no_doc_block(self) -> Dict[str, Any]:
        """
        """
        params = {}
        query = '\n' * 3
        query += """select 'This SP is a test for sources without a DocBlock'
"""
        return self.execute_row1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row0a(self, p_count: int | None) -> Any:
        """
        Test for designation type row0.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 10
        query += """select *
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_row0(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row1_conversion(self) -> Dict[str, Any]:
        """
        Test for designation type rows and type conversion.
        """
        params = {}
        query = '\n' * 5
        query += """select cast(1 as int)             as c_int
,      cast(1.1 as numeric)       as c_numeric
,      cast(2.2 as float)         as c_float
,      cast(3.3 as real)          as c_real
,      cast(4.4 as double)        as c_double
,      cast('varchar' as varchar) as c_varchar
,      cast('text' as text)       as c_text
,      cast('blob' as blob)       as c_blob
"""
        return self.execute_row1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_row1a(self, p_count: int | None) -> Dict[str, Any]:
        """
        Test for designation type row1.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 10
        query += """select *
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_row1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows1(self, p_count: int | None) -> List[Dict[str, Any]]:
        """
        Test for designation type rows.

        :param p_count: The number of rows selected.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 7
        query += """select *
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_rows(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_rows_with_index1(self, p_count: int | None) -> Dict:
        """
        Test for designation type rows_with_index.

        :param p_count: The number of rows selected.
                        RDBMS data type: int
        """
        ret = {}
        params = {'p_count': p_count}
        query = '\n' * 7
        query += """select *
from TST_FOO2
where tst_c00 <= :p_count
"""
        rows = self.execute_rows(query, params)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    ret[row['tst_c01']][row['tst_c02']].append(row)
                else:
                    ret[row['tst_c01']][row['tst_c02']] = [row]
            else:
                ret[row['tst_c01']] = {row['tst_c02']: [row]}

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton0a(self, p_count: int | None) -> int | None:
        """
        Test for designation type singleton0.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 10
        query += """select 1
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_singleton0(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton0b(self, p_count: int | None, p_value: int | None) -> bool | None:
        """
        Test for designation type singleton0 with return type bool.

        :param p_count: The number of rows selected.
                        * 0 For a valid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int
        :param p_value: The selected value.
                        RDBMS data type: int
        """
        params = {'p_count': p_count, 'p_value': p_value}
        query = '\n' * 11
        query += """select :p_value
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_singleton0(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton1a(self, p_count: int | None) -> int:
        """
        Test for designation type singleton1.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 10
        query += """select 1
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_singleton1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_singleton1b(self, p_count: int | None, p_value: int | None) -> bool:
        """
        Test for designation type singleton1 with return type bool.

        :param p_count: The number of rows selected.
                        * 0 For an invalid test.
                        * 1 For a valid test.
                        * 2 For an invalid test.
                        RDBMS data type: int
        :param p_value: The selected value.
                        RDBMS data type: int
        """
        params = {'p_count': p_count, 'p_value': p_value}
        query = '\n' * 11
        query += """select :p_value
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_singleton1(query, params)

    # ------------------------------------------------------------------------------------------------------------------
    def tst_test_yield(self, p_count: int | None) -> List[Dict[str, Any]]:
        """
        Test for designation type yield.

        :param p_count: The number of rows selected.
                        RDBMS data type: int
        """
        params = {'p_count': p_count}
        query = '\n' * 7
        query += """select *
from TST_FOO2
where tst_c00 <= :p_count
"""
        return self.execute_yield(query, params)

# ----------------------------------------------------------------------------------------------------------------------
