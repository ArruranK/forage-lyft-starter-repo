import unittest
from tire.tire import OctoprimeTire


class TestOctoprime(unittest.TestCase):
    def testNeedsService(self):
        tire = OctoprimeTire([0.75, 0.75, 0.75, 0.75])
        self.assertTrue(tire.needs_service())

    def testDoesNotNeedService(self):
        tire = OctoprimeTire([0.75, 0.75, 0.75, 0.74])
        self.assertFalse(tire.needs_service())
