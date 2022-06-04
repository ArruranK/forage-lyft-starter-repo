from serviceable import Serviceable


class Engine(Serviceable):

    def needs_service(self):
        pass


class CapuletEngine(Engine):

    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage >= 30000:
            return True
        return False


class WilloughbyEngine(Engine):

    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage >= 60000:
            return True
        return False


class SternmanEngine(Engine):

    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if self.warning_light_on:
            return True
        return False
