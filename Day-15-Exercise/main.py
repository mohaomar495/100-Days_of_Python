MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 3.00
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0
is_on = True

def is_resource_sufficient(drink):
    """returns True if resource is enough, otherwise False"""
    try:
        global resources
        for item in MENU[drink]["ingredients"]:
            if resources[item] < MENU[drink]["ingredients"][item]:
                print(f"Sorry there is not enough {item}.")
                return False
    except KeyError:
        pass
    else:
        return True


def make_coffee(drink):
    """Makes a coffee"""
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink} ☕️. Enjoy!")


def coin_processing(drink, coins):
    """Returns True if the coins are enough for exchange, otherwise False"""
    if coins >= MENU[drink]["price"]:
        change = round(coins - MENU[drink]["price"], 2)
        print(f"Here is ${change} in change")
        global money
        money += MENU[drink]["price"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")
    else:
        if is_resource_sufficient(choice):
            print("Please insert some coins: \n")
            quarters = int(input("Quarter: "))
            dimes = int(input("Dimes: "))
            nickel = int(input("Nickel: "))
            pennies = int(input("Pennies: "))
            coins = quarters * 0.25 + dimes * 0.1 + nickel * 0.05 + pennies * 0.01

            if coin_processing(choice, coins):
                make_coffee(choice)