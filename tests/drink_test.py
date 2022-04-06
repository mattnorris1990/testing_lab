import unittest

from classes.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guiness", 4)

    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("Guiness", self.drink.name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_price(self):
        self.assertEqual(4, self.drink.price)
