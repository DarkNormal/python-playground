import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def output_machine_report():
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    if "money" in resources:
        print(f"Money: ${resources.get('money')}")


def prompt_user():
    valid_input = False
    while not valid_input:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input in MENU.keys():
            drink = user_input
            valid_input = True
            return drink
        elif user_input == "off":
            print("Turning off coffee machine")
            sys.exit()
        elif user_input == "report":
            output_machine_report()


def check_resources(drink_name):
    drink = MENU[drink_name]
    resources_available = True
    for ingredient, quantity in drink.get("ingredients").items():
        if resources.get(ingredient) < quantity:
            print(f"Sorry there is not enough {ingredient}")
            resources_available = False
    return resources_available


def add_to_money(payment):
    if "money" not in resources:
        resources["money"] = payment
    else:
        resources["money"] += payment


def collect_payment(drink_name):
    drink = MENU[drink_name]
    payment_received = True
    cost = drink.get('cost')
    print(f"Price of drink is ${cost}\nPlease insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    total_coinage = quarters * 0.25 + dimes * 0.1 + nickels * 0.5 + pennies * 0.01
    if total_coinage > cost:
        rounded_amount = str(round(total_coinage - cost, 2))
        print(f"Here is ${rounded_amount} in change.")
        add_to_money(cost)
    elif total_coinage < cost:
        print("Sorry that's not enough money. Money refunded.")
        payment_received = False
    return payment_received


def produce_drink(drink_name):
    drink = MENU[drink_name]
    for ingredient, quantity in drink.get("ingredients").items():
        resources[ingredient] -= quantity
    print(f"Here is your {drink_name} ☕. Enjoy!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        user_selection = prompt_user()

        if check_resources(user_selection):
            if collect_payment(user_selection):
                produce_drink(user_selection)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/