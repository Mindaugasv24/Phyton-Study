from transports.transport.Transport import main

bus1 = Busvehicles(50, 100000, "ABC123", "diesel", 1000, "2022-01-15", "B category", 20, "2022-05-20")
bus1.technical_notice()
bus1.insurance_notice()
print(bus1.costs(500))
print(bus1.transport(200, 500))


car = EasyCar(10000, "ABC123", "Petrol", 500, ["2022-03-15", "2022-09-15"], ["B"], 6.5, "2023-01-01")
car.check_insurance_and_tech_inspection("2022-11")
car.calculate_costs_for_distance(200)
