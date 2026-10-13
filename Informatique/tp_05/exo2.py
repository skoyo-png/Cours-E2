class Airplane:
    def __init__(self, name: str):
        self.fly = False
        self.name = name

    def take_off(self):
        self.fly = True

    def land(self):
        self.fly = False

    def __str__(self):
        if self.fly:
            return f"{self.name} - flying"
        else:
            return f"{self.name} - ground"


class MilitaryAircraft(Airplane):
    def __init__(self, name: str, mission: str):
        super().__init__(name)
        self.mission = mission

    def __str__(self):
        if self.fly:
            return f"{self.name} - flying - {self.mission}"
        else:
            return f"{self.name} - ground - no mission"


class CargoAircraft(Airplane):
    def __init__(self, name: str, shipment: str):
        super().__init__(name)
        self.shipment = shipment

    def __str__(self):
        if self.fly:
            return f"{self.name} - flying - {self.shipment}"
        else:
            return f"{self.name} - ground - no shipment"


class CivilAircraft(Airplane):
    def __init__(self, name: str, passengers: int):
        super().__init__(name)
        self.passengers = passengers

    def __str__(self):
        if self.fly:
            return f"{self.name} - flying - {self.passengers} passengers"
        else:
            return f"{self.name} - ground - no passengers"






test_military_aircraft = MilitaryAircraft("Military Aircraft Mig 21", "Air Superiority")
test_military_aircraft.take_off()
print(test_military_aircraft)


test_cargo_aircraft = CargoAircraft("Cargo Aircraft Airbus A300", "contains fruits")
test_cargo_aircraft.take_off()
print(test_cargo_aircraft)


test_civil_aircraft = CivilAircraft("Civil Aircraft Airbus A300", 120)
test_civil_aircraft.take_off()
print(test_civil_aircraft)



p1 = Airplane("Airbus A380")
p2 = Airplane("Mig 21")
p1.take_off()
p2.land()
print(p1)
print(p2)
