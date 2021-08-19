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

coins = {
    "quarters": .25,
    "dimes": .10,
    "nickels": .05,
    "pennies": .01
}

user_choice = ''
money_deposited = 0
water_used = 0
milk_used = 0
coffee_used = 0
cost = 0


def get_resources():
    print(f'Water: {resources["water"] - water_used}ml')
    print(f'Milk: {resources["milk"] - milk_used}ml')
    print(f'Coffee: {resources["coffee"] - coffee_used}g')
    print(f'Money: ${money_deposited}')


def update_resources(user_choice, water_used, milk_used, coffee_used):
    if user_choice == "latte":
        water_used = water_used + MENU["latte"]["ingredients"]["water"]
        milk_used = milk_used + MENU["latte"]["ingredients"]["milk"]
        coffee_used = coffee_used + MENU["latte"]["ingredients"]["coffee"]
        return water_used, milk_used, coffee_used
    elif user_choice == "espresso":
        water_used = water_used + MENU["espresso"]["ingredients"]["water"]
        milk_used = milk_used + MENU["espresso"]["ingredients"]["milk"]
        coffee_used = coffee_used + MENU["espresso"]["ingredients"]["coffee"]
        return water_used, milk_used, coffee_used
    elif user_choice == "cappuccino":
        water_used = water_used + MENU["cappuccino"]["ingredients"]["water"]
        milk_used = milk_used + MENU["cappuccino"]["ingredients"]["milk"]
        coffee_used = coffee_used + MENU["cappuccino"]["ingredients"]["coffee"]
        return water_used, milk_used, coffee_used


def process_coins(user_choice, drink_cost):
    print("Please insert coins.")
    qty_quarters = int(input("How many quarters?:"))
    qty_dimes = int(input("How many dimes?:"))
    qty_nickels = int(input("How many nickles?:"))
    qty_pennies = int(input("How many pennies?:"))

    mon_quarters = qty_quarters * coins["quarters"]
    mon_dimes = qty_dimes * coins["dimes"]
    mon_nickels = qty_nickels * coins["nickels"]
    mon_pennies = qty_pennies * coins["pennies"]

    total_deposited = mon_quarters+mon_dimes+mon_nickels+mon_pennies

    if total_deposited >= drink_cost:
        change = total_deposited - drink_cost
        money_deposited = MENU[user_choice][cost]
        print(f"Your change is: ${change}")
        if user_choice == "latte":
            print("Here is your latte. Enjoy.")
        elif user_choice == "espresso":
            print("Here is your espresso. Enjoy.")
        else:
            print("Here is your cappuccino. Enjoy.")
        update_resources(user_choice, water_used, milk_used, coffee_used)
        return water_used, milk_used, coffee_used, money_deposited
    else:
        print("Sorry. That is not enough money. Money refunded.")
        return


def determine_cost(user_choice):
    if user_choice == "latte":
        return MENU["latte"]["cost"]
    elif user_choice == "espresso":
        return MENU["espresso"]["cost"]
    else:
        return MENU["cappuccino"]["cost"]


def check_resources(user_choice, water_used, milk_used, coffee_used):
    if (resources["water"] - water_used - MENU[user_choice]["ingredients"]["water"]) <= 0:
        print("Sorry.  There is not enough water.")
        return
    elif (resources["milk"] - milk_used - MENU[user_choice]["ingredients"]["milk"]) <= 0:
        print("Sorry.  There is not enough milk.")
        return
    elif (resources["coffee"] - coffee_used - MENU[user_choice]["ingredients"]["coffee"]) <= 0:
        print("Sorry.  There is not enough coffee.")
        return
    else:
        return


def process_command(user_choice):
    if user_choice == "report":
        get_resources()
    elif user_choice == "off":
        return
    else:
        check_resources(user_choice, water_used, milk_used, coffee_used)
        drink_cost = determine_cost(user_choice)
        process_coins(user_choice, drink_cost)


while user_choice != "off":
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    process_command(user_choice)


# TODO: 1. Ask what user would like.


# TODO: 2. Print report of all coffee machine resources


# TODO: 2. Check resources sufficient?


# TODO: 3. Process coins.


# TODO: 4. Check transaction successful?


# TODO: 5. Make Coffee.
