import unittest
from engine.engine import CapuletEngine


class TestCapulet(unittest.TestCase):
    def testNeedsService(self):
        last_service_mileage = 0
        current_mileage = 30001
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def testDoesNotNeedService(self):
        last_service_mileage = 0
        current_mileage = 30000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
