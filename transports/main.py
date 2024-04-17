from datetime import datetime

from transports.car import Car

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
