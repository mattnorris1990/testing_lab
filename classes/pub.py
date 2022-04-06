class Pub:

    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def sell_drink(self, drink_name, customer):
        customer.wallet -= self.drinks[drink_name] 
        self.till += self.drinks[drink_name]


    