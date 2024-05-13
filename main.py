from db.db_lesson import DB

db = DB()
db.create_connection_if_not_exist()

tables = [
    "CREATE TABLE IF NOT EXISTS transmision (transmision_id INTEGER PRIMARY KEY AUTOINCREMENT, transmision char, transmision_type char);",
    "CREATE TABLE IF NOT EXISTS engine(engine_id INTEGER PRIMARY KEY AUTOINCREMENT, engine_type char, cc_displacement char, Power_BHP integer, Torque_Nm integer, Fuel_type char);",
    "CREATE TABLE IF NOT EXISTS model_type(model_type_id INTEGER PRIMARY KEY AUTOINCREMENT, Make char, Body_type char, Seating_capacity integer, Fuel_tank_capacity_L integer);",
    "CREATE TABLE IF NOT EXISTS model(model_id INTEGER PRIMARY KEY AUTOINCREMENT, Car_name char, Mileage_kmpl integer, model char);",
    "CREATE TABLE IF NOT EXISTS market(market_id INTEGER PRIMARY KEY AUTOINCREMENT, Price integer, Make_year integer, color char,"
    "Milieage_run integer, No_of_owners char);",
]
for table in tables:
    db.execute_sql_query(table)

# tables2 = ["transmision", "engine", "model_type", "model", "market"]
# for table in tables2:
#     db.drop_tables_if_exits(table)

db.close_connection()

"""
INSERT INTO transmision (transmision, transmision_type) VALUES ("7 belekas", "automatic");
INSERT INTO engine (engine_type, cc_displacement, Power_BHP, Torque_Nm, Fuel_type) VALUES ("v8", "sda", "245", "fa", "petrol");
INSERT INTO model_type (Make, Body_type, Seating_capacity, Fuel_tank_capacity_L) VALUES ("1964", "sedan", "2" "60");
INSERT INTO model (Car_name, Mileage_kmpl, model) VALUES ("mustang", "180", "shelby GT 500");
INSERT INTO market (Price, Make_year, color, Milieage_run, No_of_owners) VALUES ("40000", "1964", "red", "25000", "1");
"""
