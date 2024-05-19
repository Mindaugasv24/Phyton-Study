"""
CRUD operation with database
"""

import sqlite3

from db_project_sqla.constants import URL


class DB:
    """representing """
    def __init__(self, url=URL):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def execute_sql_query(self, sql_query: str) -> None:
        """
        representing: sends sql query to database
        :param sql_query: row sql query in string format
        :return: None
        """
        self.cursor.execute(sql_query)
        self.connection.commit()
        print('SQL executed')

    def execute_sql_query_and_return_values(self, sql_query: str) -> list[tuple]:
        """representing: """
        return self.cursor.execute(sql_query).fetchall()

    def drop_table(self, table: str) -> None:
        """representing tables drop in database"""
        sql_query = f"drop table if exists {table}"
        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_transmission_table(self, **kwargs) ->None:
        """
        INSERT INTO table_name (column1, column2, column3, ...)
        VALUES (value1, value2, value3, ...);
        :param kwargs:
        :return:
        """
        sql_query = f"""
        INSERT INTO table_name (transmission, transmission_type)
        VALUES ("{kwargs['transmission']}", "{kwargs['transmission_type']}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def read_data_from_table(self, table: str) -> list[tuple]:
        """read data from tables"""
        sql_query = f"select * from {table}"
        return self.execute_sql_query_and_return_values(sql_query=sql_query)

    def close_connection(self):
        """representing connection bonds who closed"""
        self.connection.close()
