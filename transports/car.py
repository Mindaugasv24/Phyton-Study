from datetime import datetime

from transports.auto import Auto

class Car(Auto):
    """Class representing a transport type"""
    def __init__(self, km_per_year, car_registration_number, fuel_type, fixed_costs, technical_inspections_date,
                 license_categories, fuel_consumption_100_km, insurance_date):
        super().__init__(km_per_year, car_registration_number, fuel_type, fixed_costs, technical_inspections_date,
                         license_categories, fuel_consumption_100_km, insurance_date)

# def run():
#     print(run)
# def check(self):
#     print('Check')