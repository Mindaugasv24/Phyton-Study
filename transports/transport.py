class Transport: """ Class representing a transport"""
    def __init__(self, plate_number: str, distance: int, expenses: int, fueltype: str,
        technical_date: str, licence_category: str, insurance_date: str, fuel_consumption: int):
        self.expenses = expenses
        self.licence_category = licence_category
        self.fuel_consumption = fuel_consumption
        self.insurance_date = insurance_date
        self.fueltype = fueltype
        self.technical_date = technical_date
        self.plate_number = plate_number
        self.distance = distance
