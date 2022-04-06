import unittest

from classes.food import *

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Chips", 5, 1)

    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("Chips", self.food.name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_price(self):
        self.assertEqual(5, self.food.price)