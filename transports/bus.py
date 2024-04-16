from datetime import datetime, timedelta

from transports.transport import Transport


class Busvehicles(Transport): """ Class represented a transport type"""
    def __init__(
        self,
        plate_number: str,
        distance: int,
        expenses: int,
        fueltype: str,
        technical_date: datetime,
        licence_category: str,
        insurance_date: str,
        fuel_consumption: int,
    ):
        super().__init__(
            plate_number,
            distance,
            expenses,
            fueltype,
            technical_date,
            licence_category,
            insurance_date,
            fuel_consumption,
        )

    def reikia_draudimo(self):
        # papildomas metodas tik autobusui, kuris patikrina ar reikia is naujo sudaryti draudimo sutarti,
        # pagal vietu skaiciu ir kilometrazo rodiklius
        pass

    def keleiviu_skaicius(self, keleiviai):
        # metodas, kuris apskaiciuoja kiek reikia autobusu norint pervezti N keleiviu
        pass

    def bendra_suma(self, keleiviai, atstumas):
        # metodas kuris paskaiciuoja kokia butu bendra suma, pervezus N keleiviu ir nuvaziavus atstuma X
        pass
