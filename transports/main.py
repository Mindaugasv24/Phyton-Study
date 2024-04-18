from datetime import datetime

from transports.car import Car

from transports.bus import Bus


bus = Bus(
    km_per_year=20000,
    car_registration_number="ANB205",
    fuel_type="Petrol",
    fixed_costs=4000,
    technical_inspections_date=datetime(year=2024, month=5, day=15),
    license_categories="B",
    fuel_consumption_100_km=8,
    insurance_date=datetime(year=2024, month=5, day=15),
    passengers_per_bus=50
)
total_cost_per_passenger = bus.total_cost_for_transporting_passengers(50, 200)
print(total_cost_per_passenger)


# bus = Bus(
#     km_per_year=20000,
#     car_registration_number="ANB205",
#     fuel_type="Petrol",
#     fixed_costs=4000,
#     technical_inspections_date=datetime(year=2024, month=5, day=15),
#     license_categories="B",
#     fuel_consumption_100_km=8,
#     insurance_date=datetime(year=2024, month=5, day=15),
#     number_of_passengers=150
# )
#
# buses_needed = bus.number_of_buses_to_transport_passengers(number_of_passengers)
# print(f"Number of buses needed to transport {self.number_of_passengers} passengers: {buses_needed}")



car = Car(
    km_per_year=20000,
    car_registration_number="ANB205",
    fuel_type="Petrol",
    fixed_costs=4000,
    technical_inspections_date=datetime(year=2024, month=5, day=15),
    license_categories="B",
    fuel_consumption_100_km=8,
    insurance_date=datetime(year=2024, month=5, day=15),
)

print(car.check_if_next_month_needs_insurance())
print(car.check_if_next_month_needs_technical())

# car.run()
# car.check()