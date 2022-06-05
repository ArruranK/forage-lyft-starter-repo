import unittest
from datetime import date
from battery.battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def testNeedsService(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=self.year - 2)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def testDoesNotNeedService(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=self.year - 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
