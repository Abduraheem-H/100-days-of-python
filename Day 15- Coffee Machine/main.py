from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Drinks = Menu()
Coffee = CoffeeMaker()
Money = MoneyMachine()


is_working = True

while is_working:
    choice = input(f"What would you like?({Drinks.get_items()})").lower()
    if choice == "off":
        is_working = False
    elif choice == "report":
        Coffee.report()
    else:
        drink = Drinks.find_drink(choice)
        if Coffee.is_resource_sufficient(drink):
            if Money.make_payment(drink.cost):
                Coffee.make_coffee(drink)
# The code above is a simple coffee machine simulator that allows users to order drinks, check resources, and make payments.
# It uses classes to manage the coffee machine's resources, menu items, and payment processing.
