from serviceable import Serviceable


class Tire(Serviceable):

    def needs_service(self):
        pass


class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for i in range(4):
            if (self.tire_wear[i] >= 0.9):
                return True
        return False


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        sum = 0
        for i in range(4):
            sum += self.tire_wear[i]
        return sum >= 3
