from car import Car
from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery.battery import NubbinBattery, SpindlerBattery
from tire.tire import CarriganTire, OctoprimeTire


class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
