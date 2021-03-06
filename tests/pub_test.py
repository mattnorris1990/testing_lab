import unittest

from classes.pub import *
from classes.drink import *
from classes.customer import *
from classes.food import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Jim", 20, 30)
        self.customer_2 = Customer("Brian", 10, 16)
        self.customer_3 = Customer("Lola", 30, 32)
        self.customer_4 = Customer("Naomi", 10, 10)
        self.drink_1 = Drink("Guiness", 4, 1)
        self.drink_2 = Drink("Tennents", 3, 2)
        self.drink_3 = Drink("Red Wine", 5, 5)
        # self.drinks_list = [self.drink_1, self.drink_2, self.drink_3]

        self.drinks_dict = [
            { "drink" : self.drink_1,
            "quantity" : 10 },
            { "drink" : self.drink_2,
            "quantity" : 15 },
            { "drink" : self.drink_3,
            "quantity" : 20 }
        ]

        self.food_1 = Food("Chips", 5, 1)
        # self.pub = Pub("The CodeClan Cubby", 100, self.drinks_list)
        self.pub = Pub("The CodeClan Cubby", 100, self.drinks_dict)



    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("The CodeClan Cubby", self.pub.name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_till(self):
        self.assertEqual(100, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_has_drinks(self):
        # self.assertEqual(self.drinks_list, self.pub.drinks)
        self.assertEqual(self.drinks_dict, self.pub.drinks)

    # @unittest.skip("Delete this line to run the test")
    def test_sell_drink(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(16, self.customer_1.wallet)
        self.assertEqual(104, self.pub.till)

    
    # @unittest.skip("Delete this line to run the test")  
    def test_customer_over_18_and_not_drunk(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(16, self.customer_1.wallet)
        self.assertEqual(104, self.pub.till)
        self.assertEqual(1, self.customer_1.drunkenness)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_under_18_and_not_drunk(self):
        self.pub.sell_drink(self.drink_1, self.customer_2)
        self.assertEqual(10, self.customer_2.wallet)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(0, self.customer_2.drunkenness)
        self.assertEqual("You don't have to go home, but you can't stay here!", self.pub.sell_drink(self.drink_1, self.customer_2))

    # @unittest.skip("Delete this line to run the test")
    def test_customer_under_18_and_not_drunk(self):
        self.pub.sell_drink(self.drink_3, self.customer_3)
        self.pub.sell_drink(self.drink_3, self.customer_3)
        self.assertEqual(25, self.customer_3.wallet)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(5, self.customer_3.drunkenness)
        self.assertEqual("You don't have to go home, but you can't stay here!", self.pub.sell_drink(self.drink_1, self.customer_3))
    
    # @unittest.skip("Delete this line to run the test")
    def test_sell_food(self):
        self.pub.sell_food(self.food_1, self.customer_3)
        self.assertEqual(25, self.customer_3.wallet)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(0, self.customer_3.drunkenness)
        self.pub.sell_drink(self.drink_3, self.customer_3)
        self.pub.sell_food(self.food_1, self.customer_3)
        self.assertEqual(4, self.customer_3.drunkenness)

    def test_stock_value(self):
        self.pub.stock_value()
        self.assertEqual(185, self.pub.total_value)
