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
        sql_query = f"""
            Insert into transmision (transmision, transmision_type) values
            ("{kwargs["transmision"]}", "{kwargs["transmision_type"]}");
        """
        print(sql_query)
        self.execute_sql_query(sql_query)

    def add_data_market(self, **kwargs):
        """representing data of market"""
        # price = kwargs.get("price", 40000)
        # make_year = kwargs.get("make_year", 1964)
        # color = kwargs.get("color", None)
        # Milieage_run = kwargs.get("Milieage_run", 25000)
        sql_query = f"""
            Insert into market (Price, make_year, color, Milieage_run) values
            ("{kwargs["price"]}", "{kwargs["make_year"]}", "{kwargs["color"]}", "{kwargs["Milieage_run"]}");
        """
        print(sql_query)
        self.execute_sql_query(sql_query)

    def add_data_engine(self, **kwargs):
        """representing data of engine"""
        # engine_type = kwargs.get("engine_type", "petrol"),
        # cc_displacement = kwargs.get("cc_displacement", "petrol"),
        # Power_BHP = kwargs.get("Power_BHP", "240"),
        # Torque_Nm = kwargs.get("Torque_Nm", "240"),
        # Fuel_type = kwargs.get("Fuel_type", "petrol"),
        sql_query = f"""
            Insert into engine (engine_type, cc_displacement, Power_BHP, Torque_Nm, Fuel_type) values
            ("{kwargs["engine_type"]}", "{kwargs["cc_displacement"]}", "{kwargs["Power_BHP"]}", "{kwargs["Torque_Nm"]}",
            "{kwargs["Fuel_type"]}");
        """
        print(sql_query)
        self.execute_sql_query(sql_query)

    def add_data_model_type(self, **kwargs):
        """representing data of model_type"""
        # make = (kwargs.get("make", 1945),)
        # body_type = (kwargs.get("body_type", "sedan"),)
        # seating_capacity = (kwargs.get("seating_capacity", 4),)
        # fuel_tank_capacity_L = kwargs.get("fuel_tank_capacity_L", 70)
        sql_query = f"""
            Insert into model_type (make, body_type, seating_capacity, fuel_tank_capacity_L) values
            ("{kwargs["make"]}", "{kwargs["body_type"]}", "{kwargs["seating_capacity"]}",
            "{kwargs["fuel_tank_capacity_L"]}");
        """
        print(sql_query)
        self.execute_sql_query(sql_query)
    def add_data_model(self, **kwargs):
        """representing data of model"""
        # Car_name = kwargs.get("Car_name", "mustang")
        # Mileage_kmpl = kwargs.get("Mileage_kmpl", 180)
        # model = kwargs.get("model", "shelby GT 500")
        sql_query = f"""
                    Insert into model (Car_name, Mileage_kmpl, model) values
                    ("{kwargs["Car_name"]}", "{kwargs["Mileage_kmpl"]}", "{kwargs["model"]}");
        """
        print(sql_query)
        self.execute_sql_query(sql_query)

    def drop_tables_if_exits(self, table):
        """representing db tables"""
        sql_query = f"if exist drop_table {table}"
        self.execute_sql_query(sql_query)
        self.cursor.commit()

    def delete_row_from_table(self, data: dict) -> None:
        """representing delete data from the row in table"""
        sql_query = f"""
        DELETE FROM {data['table']}"
        WHERE {data['column_name']} in {data['column_values']};
        """
        self.execute_sql_query(sql_query=sql_query)

    def close_connection(self):
        self.conection.close()