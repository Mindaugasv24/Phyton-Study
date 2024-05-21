from typing import Literal

from sqlalchemy import create_engine
import pandas as pd
from pandas import DataFrame

from db_exercise.constant import URL, FILE_URL


class PandasDB:
    def __init__(self, file_name: str = FILE_URL, url: str = URL):
        self.data = pd.read_excel(file_name)
        self.data.drop_duplicates()
        self.engine = create_engine(url)

    def print_info(self):
        """execute info"""
        print(self.data.info())
        print(self.data.head())

    def read_data_from_DB(self, table_name: str) -> DataFrame:
        """read data from database"""
        return pd.read_sql_table(table_name=table_name, con=self.engine)

    def create_table_in_DB(
        self,
        data: DataFrame,
        index_label: str,
        table_name: str,
        if_exists: Literal["fail", "replace", "append"] = "replace",
    ) -> None:
        """create table in database"""
        data.to_sql(
            name=table_name,
            con=self.engine,
            index=True,
            index_label=index_label,
            if_exists=if_exists,
        )

    def create_transmission_table(self):
        """create table for transmission"""
        transmission = self.data[["transmission", "transmission_Type"]]
        transmission.drop_duplicates(inplace=True)
        transmission.reset_index(inplace=False, drop=True)
        self.create_table_in_DB(
            transmission, "transmissions", index_label="transmission_id"
        )

    def merge_transmission_table_with_main_table(self):
        """representing tables merging"""
        transmission_data = self.read_data_from_DB("transmission")
        self.data = self.data.merge(
            transmission_data, how="inner", on=["transmission", "transmission_type"]
        )
        self.data.rename(columns={"index": "transmission_id"}, inplace=True)
        self.data.drop(columns=["transmission", "transmission_type"], inplace=True)

    def create_engine_table(self):
        """create engine table
        add: engine_id, engine_type, cc_displacement, power_bhp, torque_nm, fuel_type
        """
        engine = self.data[
            ["engine_type", "cc_displacement", "power_bhp", "torque_nm", "fuel_type"]
        ]
        engine.drop_duplicates(inplace=True)
        engine.reset_index(inplace=False, drop=True)
        self.create_table_in_DB(engine, "engines", index_label="engine_id")

    def change_data__frame_columns_names(self):
        """representing table columns"""
        self.data.rename(mapper=COLUMNS_NAMES, implace=True, axis="columns")
        return self.data

    def merge_transmission_table_with_main_table(self):
        """representing tables merging"""
        engine_data = self.read_data_from_DB("engines")
        self.data = self.data.merge(
            engine_data,
            how="inner",
            on=[
                "engine_type",
                "cc_displacement",
                "power_bhp",
                "torque_nm",
                "fuel_type",
            ],
        )
        self.data.drop(
            columns=[
                "engine_type",
                "cc_displacement",
                "power_bhp",
                "torque_nm",
                "fuel_type",
            ],
            inplace=True,
        )

    def read_from_excel_and_create_table_in_DB(self, data: dict) -> DataFrame:
        """representing:"""
        data_frame = self.data[[data["columns"]]]
        data_frame.drop_duplicates(inplace=True)
        self.create_table_in_DB(
            data_frame, data["table_name"], f'{data["table_name"]}_id'
        )
        table = self.read_data_from_DB(data["table_name"])
