from datetime import datetime

from transports.transport import Transport

class Lightvehicles(Transport): """Class representing a transport type"""
    def __init__(self, number_of_seats, km_per_year, car_number, fuel_type, fixed_costs, technical_inspection_date,
             license_categories, fuel_consumption_100km, insurance_date, annual_mileage, reg_number):
        self.number_of_seats = number_of_seats
        self.km_per_year = km_per_year
        self.car_number = car_number
        self.fuel_type = fuel_type
        self.fixed_costs = fixed_costs
        self.technical_inspection_date = technical_inspection_date
        self.license_categories = license_categories
        self.fuel_consumption_100km = fuel_consumption_100km
        self.insurance_date = insurance_date
        self.annual_mileage = annual_mileage
        self.reg_number = reg_number

    def check_insurance_and_tech_inspection(self, next_month):
        if next_month in self.tech_inspection_dates:
            print("Technical inspection is required next month.")
        if self.insurance_date == next_month:
            print("Insurance renewal is required next month.")

    def calculate_costs_for_distance(self, distance):
        variable_costs = distance * (self.annual_mileage / 100)
        total_costs = variable_costs + self.fixed_costs
        print(f"The total costs for driving {distance} kilometers will be {total_costs} euros.")