import unittest

from classes.customer import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Mark", 20, 0)

    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("Mark", self.customer.name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)