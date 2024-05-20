from typing import Literal

from sqlalchemy import create_engine
import pandas as pd
from pandas import DataFrame

from db_exercise.constant import URL, FILE_URL


class PandasDB:
    def __init__(self, file_name: str = FILE_URL, url: str = URL):
        self.data = pd.read_execute(file_name)
        self.data.drop_duplicates()
        self.engene = create_engine(url)

    def print_info(self):
        """execute info"""
        print(self.data.info())
        print(self.data.head())

    def read_data_from_DB(self, table_name: str) -> DataFrame:
        """read data from database"""
        return pd.read_sql_table(table_name=table_name, con=self.engene)


    def create_table_in_DB(
        self,
        data: DataFrame,
        table_name: str,
        if_exists: Literal["fail", "replace", "append"] = "replace",
    ) -> None:
        """create table in database"""
        data.to_sql(name=table_name, con=self.engine, index=True, if_exists=if_exists)

    def create_transmission_table(self):
        """create table for transmission"""
        transmission = self.data[["Transmission", "Transmission_Type"]]
        transmission.drop_duplicates(inplace=True)
        transmission.reset_index(inplace=False, drop=True)
        self.create_table_in_DB(transmission, "transmissions")

    def merge_transmission_table_with_main_table(self):
        """representing tables merging"""
        transmission_data = self.read_data_from_DB("transmission")
        new_data = self.data.merge(
            transmission_data, how="inner", on=["Transmission", "Transmission_Type"]
        )
        new_data.rename(columns={"index": "transmission_id"}, inplace=True)
        new_data.drop(columns=["Transmission", "Transmission_Type"], inplace=True)
        print(new_data.Head(50))
