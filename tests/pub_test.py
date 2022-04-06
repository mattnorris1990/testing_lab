import unittest

from classes.pub import *
from classes.drink import *
from classes.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_dict = {
            "Guiness" : 4,
            "Tennents" : 3,
            "Red Wine" : 5,
            "White Wine" : 5
        }
        self.pub = Pub("The CodeClan Cubby", 100, self.drink_dict)

    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("The CodeClan Cubby", self.pub.name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_till(self):
        self.assertEqual(100, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_has_drinks(self):
        self.assertEqual(self.drink_dict, self.pub.drinks)

    # @unittest.skip("Delete this line to run the test")
    def test_sell_drink(self):
        customer = Customer("Jim", 20)
        self.pub.sell_drink("Guiness", customer)
        self.assertEqual(16, customer.wallet)
        self.assertEqual(104, self.pub.till)
