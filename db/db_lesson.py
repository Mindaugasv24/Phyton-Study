import sqlite3


class DB:
    """representing data base"""

    def __init__(self, url="duomenu_baze.db"):
        self.url = url
        self.cursor = None
        self.conection = None

    def create_connection_if_not_exist(self):
        """representing connect to the database"""
        self.conection = sqlite3.connect(self.url)
        self.cursor = self.conection.cursor()

    def close_connection(self):
        """representing closed connection"""
        self.cursor.close()

    def execute_sql_query(self, query):
        """representing sql run"""
        self.cursor.execute(query)
        self.conection.commit()

    def add_data_transmision(self, **kwargs):
        """representing data of transmision"""
        sql_query = (
            f"Insert into (transmision, transmision_type) "
            f'values ("{kwargs["transmision"]}", "{kwargs["transmision_type"]}")'
        )
        self.execute_sql_query(sql_query)

    def drop_tables_if_exits(self, table):
        """representing db tables"""
        sql_query = f"if exist drop_table {table}"
        self.execute_sql_query(sql_query)
        self.cursor.commit()
