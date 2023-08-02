import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0, 1.2, 0.9, 1.5]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0, 0.2, 0, 0.5]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())