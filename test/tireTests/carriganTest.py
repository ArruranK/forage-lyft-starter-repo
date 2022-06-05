import unittest
from tire.tire import CarriganTire


class TestCarrigan(unittest.TestCase):
    def testNeedsService(self):
        tire = CarriganTire([0, 0, 0, 0.9])
        self.assertTrue(tire.needs_service())

    def testDoesNotNeedService(self):
        tire = CarriganTire([0.2, 0.3, 0.4, 0.5])
        self.assertFalse(tire.needs_service())
