from datetime import datetime, timedelta

from transports.transport import Transport


class Truckvehicles(Transport): """ Class represented a transport type"""
    def __init__(
        self,
        plate_number: str,
        distance: int,
        expenses: int,
        fueltype: str,
        technical_data: datetime,
        licence_category: str,
        insurance_date: str,
        fuel_consumption: int,
    ):
        super().__init__(
            plate_number,
            distance,
            expenses,
            fueltype,
            technical_data,
            licence_category,
            insurance_date,
            fuel_consumption,
        )

    def reisu_skaicius(self, kroviniai):
        # metodas kuris paskaiciuoja kiek reisu reikia padaryti ir ar reikia prikabinti priekaba
        pass
