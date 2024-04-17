from datetime import datetime

from transports.transport import Transport


class Truckvehicles(Transport): """ Class represented a transport type"""
    def __init__(self, number_of_seats, km_per_year, car_number, fuel_type, fixed_costs, technical_inspection_date,
             license_categories, fuel_consumption_100km, insurance_date):
        self.number_of_seats = number_of_seats
        self.km_per_year = km_per_year
        self.car_number = car_number
        self.fuel_type = fuel_type
        self.fixed_costs = fixed_costs
        self.technical_inspection_date = technical_inspection_date
        self.license_categories = license_categories
        self.fuel_consumption_100km = fuel_consumption_100km
        self.insurance_date = insurance_date