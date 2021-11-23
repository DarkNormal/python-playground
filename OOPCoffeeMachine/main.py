from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys


def prompt_user(coffee_maker, money_machine):
    coffee_menu = Menu()
    valid_input = False
    while not valid_input:
        user_input = input(f"What would you like? ({coffee_menu.get_items()}): ")
        if user_input == "off":
            print("Turning off coffee machine")
            sys.exit()
        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = coffee_menu.find_drink(user_input)
            if drink is not None:
                valid_input = True
                return drink


if __name__ == '__main__':
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        user_selection = prompt_user(coffee_maker, money_machine)
        if coffee_maker.is_resource_sufficient(user_selection):
            if money_machine.make_payment(user_selection.cost):
                coffee_maker.make_coffee(user_selection)
