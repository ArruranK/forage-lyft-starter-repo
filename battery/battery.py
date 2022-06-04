from serviceable import Serviceable
from datetime import datetime


class Battery(Serviceable):

    def needs_service(self):
        pass


class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if (service_threshold_date < datetime.today().date()):
            return True
        return False


class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2)
        if (service_threshold_date < datetime.today().date()):
            return True
        return False
