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

# def check_insurance_and_tech_inspection(self, next_month):
#     if next_month in self.tech_inspection_dates:
#         print("Technical inspection is required next month.")
#     if self.insurance_date == next_month:
#         print("Insurance renewal is required next month.")
# def calculate_costs_for_distance(self, distance):
#     variable_costs = distance * (self.annual_mileage / 100)
#     total_costs = variable_costs + self.fixed_costs
#     print(f"The total costs for driving {distance} kilometers will be {total_costs} euros.")