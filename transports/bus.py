from datetime import datetime

from transports.auto import Auto

class Bus(Auto):
    """ Class represented a transport type"""
    def __init__(self, km_per_year, car_registration_number, fuel_type, fixed_costs, technical_inspections_date,
                 license_categories, fuel_consumption_100_km, insurance_date, passengers_per_bus):
        super().__init__(km_per_year, car_registration_number, fuel_type, fixed_costs, technical_inspections_date,
                         license_categories, fuel_consumption_100_km, insurance_date)
        self.passengers_per_bus = passengers_per_bus

    def number_of_buses_to_transport_passengers(self, number_of_passengers):
        buses_needed = number_of_passengers // self.passengers_per_bus
        if number_of_passengers % self.passengers_per_bus != 0:
            buses_needed += 1
        return buses_needed

    def total_cost_for_transporting_passengers(self, number_of_passengers, distance, fuel_price_per_litre):
        return self.calculate_costs_for_distance(distance, fuel_price_per_litre) * self.number_of_buses_to_transport_passengers(number_of_passengers)

    def total_cost_for_transporting_passengers(self, number_of_passengers,distance):
        fuel_cost = self.fuel_consumption_100_km * distance / 100 * self.fuel_type.price_per_liter
        maintenance_cost = self.fixed_costs.maintenance_cost_per_year / self.km_per_year * distance
        insurance_cost = self.fixed_costs.insurance_cost_per_year / self.km_per_year * distance
        total_cost = fuel_cost + maintenance_cost + insurance_cost
        cost_per_passenger = total_cost / number_of_passengers
        return cost_per_passenger