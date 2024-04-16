from datetime import datetime, timedelta

from transports.transport import Transport

class Lightvehicles(Transport): """Class representing a transport type"""
    def __init__(self, plate_number: str, distance: int, expenses: int, fueltype: str, technical_date: datetime,
        licence_category: str, insurance_date: str, fuel_consumption: int):
        super().__init__(plate_number, distance, expenses, fueltype, technical_date, licence_category, insurance_date,
        fuel_consumption)

    def reikia_tech_apziuros(self):
        # metodas, kuris patikrina ar reikia atlikti technine apziura sekantiems metams
        pass

    def reikia_draudimo(self):
        # metodas, kuris patikrina ar reikia is naujo sudaryti draudimo sutarti
        pass

    def skaiciuoti_kastus(self, atstumas):
        # metodas, kuris paskaiciuoja kiek kainuos nuvaziuoti tam tikra atstuma
        pass
