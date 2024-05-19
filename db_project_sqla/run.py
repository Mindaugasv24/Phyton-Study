from db_project_sqla.constants import TABLES, DROP_TABLES
from db_project_sqla.table_data import TRANSMISSION_DATA

# CRUD

from db_project_sqla.db import DB

db = DB()

for table in DROP_TABLES:
    db.drop_table(table=table)

for table_query in TABLES:
    db.execute_sql_query(table_query)

for data in TRANSMISSION_DATA:
    db.add_values_to_transmission_table(**data)


data = db.read_data_from_table('transmission')
print(data)


data = {
    'table': 'transmission',
    'values': {
        'transmission': '1 gear',
        'transmission_type': 'auto'
    },
    'where': 'where transmission_id = 3'
}

data = {
    'table': 'transmission',
    'values': {
        'one_more_column': 'bandymas'
    },
    'where': 'where transmission_id = 2'
}
db.update_value_in_table(data)


data = {
    'table': 'transmission',
    'column_name': 'transmission_id',
    'column_values': (1, 3, 5),
}

db.delete_rows_from_table(data)

db.close_connection()
