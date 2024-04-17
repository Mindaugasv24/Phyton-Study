from datetime import datetime

from transports.transport import Transport

class Busvehicles(Transport): """ Class represented a transport type"""
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

    def technical_notice(self):
        today = datetime.now()
        technical_inspection_date = datetime.strptime(self.technical_inspection_date, "%Y-%m-%d")
        if today.month != technical_inspection_date.month:
            print("Technical inspection is required this month")
        else:
            print("Technical inspection is required next month")

    def insurance_notice(self):
        today = datetime.now()
        insurance_date = datetime.strptime(self.insurance_date, "%Y-%m-%d")
        if today.month != insurance_date.month:
            print("Insurance needs to be renewed this month")
        else:
            print("Insurance needs to be renewed next month")

    def costs(self, distance):
        fuel_cost = distance / 100 * self.fuel_consumption_100km
        total_costs = fuel_cost + self.fixed_costs
        return total_costs

    def transport(self, passengers, distance):
        number_of_buses = passengers // self.number_of_seats + 1
        total_amount = number_of_buses * self.costs(distance) * self.km_per_year / distance
        return total_amount