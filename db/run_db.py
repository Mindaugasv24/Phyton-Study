from db.db_lesson import DB

db = DB()
db.create_connection_if_not_exist()

tables = [
    "CREATE TABLE IF NOT EXISTS transmision (transmision_id INTEGER PRIMARY KEY AUTOINCREMENT, transmision char, transmision_type char);",
    "CREATE TABLE IF NOT EXISTS engine(engine_id INTEGER PRIMARY KEY AUTOINCREMENT, engine_type char, cc_displacement char, Power_BHP integer, Torque_Nm integer, Fuel_type char);",
    "CREATE TABLE IF NOT EXISTS model_type(model_type_id INTEGER PRIMARY KEY AUTOINCREMENT, make char, body_type char, seating_capacity integer, fuel_tank_capacity_L integer);",
    "CREATE TABLE IF NOT EXISTS model(model_id INTEGER PRIMARY KEY AUTOINCREMENT, Car_name char, Mileage_kmpl integer, model char);",
    "CREATE TABLE IF NOT EXISTS market(market_id INTEGER PRIMARY KEY AUTOINCREMENT, price integer, make_year integer, color char, Milieage_run integer, no_of_owners char);",
]
# for table in tables:
#     db.execute_sql_query(table)

# tables2 = ["transmision", "engine", "model_type", "model", "market"]
# for table in tables2:
#     db.drop_tables_if_exits(table)

# db.close_connection()

transmisions = [
    {"transmision": "six gear", "transmision_type": "aumatik"},
    # {"transmision": "four gear", "transmision_type": "manual"},
    # {"transmision": "five gear", "transmision_type": "aumatik"},
    # {"transmision": "two gear", "transmision_type": "aumatik"},
]
for i in transmisions:
    db.add_data_transmision(**i)

markets = [
    {
        "price": 40000,
        "make_year": 1964,
        "color": "red",
        "Milieage_run": 25000,
    },
    {
        "price": 45000,
        "make_year": 1955,
        "color": "blue",
        "Milieage_run": 22000,
    },
    {
        "price": 48000,
        "make_year": 1974,
        "color": "yellow",
        "Milieage_run": 2000,
    },
    {
        "price": 35000,
        "make_year": 1994,
        "color": "black",
        "Milieage_run": 21000,
    },
]
for i in markets:
    db.add_data_market(**i)

engines = [
    {
        "engine_type": "petrol",
        "cc_displacement": "petrol",
        "Power_BHP": 240,
        "Torque_Nm": 240,
        "Fuel_type": "petrol",
    },
    {
        "engine_type": "petrol",
        "cc_displacement": "petrol",
        "Power_BHP": 240,
        "Torque_Nm": 240,
        "Fuel_type": "petrol",
    },
    {
        "engine_type": "petrol",
        "cc_displacement": "petrol",
        "Power_BHP": 240,
        "Torque_Nm": 240,
        "Fuel_type": "petrol",
    },
]

for i in engines:
    db.add_data_engine(**i)

model_types = [
    { "make": 1945, "body_type": "sedan", "seating_capacity": 4, "fuel_tank_capacity_L": 70},
    { "make": 1945, "body_type": "sedan", "seating_capacity": 4, "fuel_tank_capacity_L": 70},
    { "make": 1945, "body_type": "sedan", "seating_capacity": 4, "fuel_tank_capacity_L": 70},
    { "make": 1945, "body_type": "sedan", "seating_capacity": 4, "fuel_tank_capacity_L": 70},
]

for i in model_types:
    db.add_data_model_type(**i)

models = [
    {"Car_name": "mustang", "Mileage_kmpl": 190, "model": "shelby GT 500"},
    {"Car_name": "dodge", "Mileage_kmpl": 200, "model": "chalenger"},
    {"Car_name": "mazda", "Mileage_kmpl": 260, "model": 3},
]

for i in models:
    db.add_data_model(**i)

# data = {
#     'table': 'transmission',
#     'column_name': 'transmission_id',
#     'column_values': (1, 3, 5),
# }

# db.delete_row_from_table(data)
