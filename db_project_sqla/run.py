import sqlite3

from db_project_sqla.constants import TABLES, DROP_TABLES
from db_project_sqla.table_data import TRANSMISSION_DATA

# CRUD

from db_project_sqla.db import DB

db = DB()

for table in DROP_TABLES:
    db.drop_table(table=table)

for table_query in TABLES:
    db.execute_sql_query(table_query)

for table_query in TRANSMISSION_DATA:
    db.add_values_to_transmission_table(**data)

data = db.read_data_from_table('transmission')
print(data)

result = [d for d in data if d[2] == 'Automatic']
print(result)
