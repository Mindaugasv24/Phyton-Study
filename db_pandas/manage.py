from db_pandas.pandas_project import PandasDB

panda_db = PandasDB()

# panda_db.print_info()
# panda_db.change_data__frame_columns_names()
# panda_db.create_transmission_table()
# panda_db.create_engine_table()
# panda_db.merge_transmission_table_with_main_table()
# panda_db.read_data_from_DB('transmissions')

table_engine = {
    "table_name": "engine",
    "columns": ["engine_type", "cc_displacement", "power_bhp", "torque_nm", "fuel_type"]
}

tables = [
    table_engine
]

for table in tables:
    panda_db.read_from_excel_and_create_table_in_DB(table)
panda_db.print_info()
