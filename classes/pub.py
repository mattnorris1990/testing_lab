
class Pub:

    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks
        self.total_value = 0

    def sell_drink(self, drink, customer):
        if customer.age > 18:
            if customer.drunkenness < 5:
                customer.wallet -= drink.price
                self.till += drink.price
                customer.drunkenness += drink.alcohol_level
            else:
                return "You don't have to go home, but you can't stay here!"
        else:
            return "Go to the cafe on the other side of the street!"

    def sell_food(self, food, customer):
        customer.wallet -= food.price
        self.till += food.price
        if customer.drunkenness > 0:
            customer.drunkenness -= food.rejuvenation_level
    
    def stock_value(self):

        for drinkies in self.drinks:
            self.total_value += drinkies["quantity"] * drinkies["drink"].price
        return self.total_value