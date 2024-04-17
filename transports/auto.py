from datetime import datetime, timedelta

class Auto:
    """ Class representing a transport"""
    def __init__(self, km_per_year, car_registration_number, fuel_type, fixed_costs, technical_inspections_date, license_categories, fuel_consumption_100_km, insurance_date):
        self.insurance_date = insurance_date
        self.fuel_consumption_100_km = fuel_consumption_100_km
        self.license_categories = license_categories
        self.technical_inspections_date = technical_inspections_date
        self.fixed_costs = fixed_costs
        self.fuel_type = fuel_type
        self.car_registration_number = car_registration_number
        self.km_per_year = km_per_year

    def __check_next_month(self, date: datetime):
        today = datetime.today()
        next_month = today.replace(day=1) + timedelta(35)
        two_month_next = today.replace(day=1) + timedelta(65)

        if (
            datetime(year=next_month.year, month=next_month.month, day=1)
            <= date
            < datetime(year=two_month_next.year, month=two_month_next.month, day=1)
        ):
            return True
        return False

    def check_if_next_month_needs_technical(self):
        if self.__check_next_month(self.technical_inspections_date):
            return True
        return False

    def check_if_next_month_needs_insurance(self):
        if self.__check_next_month(self.insurance_date):
            return True
        return False