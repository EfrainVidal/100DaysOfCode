MENU = {"espresso": {"ingredients": {"water": 50,"coffee": 18,}, "cost": 1.5,},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, },"cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water_reserve = resources['water']
milk_reserve = resources['milk']
coffee_reserve = resources['coffee']
profit = 0.00


def coffee_cost(user_choice):
    """Gets the cost of each ingredient adn returns it based on coffee choice"""
    cost = MENU[user_choice]['cost']
    water = MENU[user_choice]['ingredients']['water']
    coffee = MENU[user_choice]['ingredients']['coffee']
    if user_choice == 'espresso':
        milk = 0
    else:
        milk = MENU[user_choice]['ingredients']['milk']
    return [cost, water, coffee, milk]


def calculate_money():
    """adds up all the change the user entered and returns ir"""
    print('Please insert coins.')
    quarters = .25 * float(input("how many quarters?: "))
    dimes = .10 * float(input("how many dimes?: "))
    nickles = .05 * float(input("how many nickles?: "))
    pennies = .01 * float(input("how many pennies?: "))

    money_received = quarters + dimes + nickles + pennies
    return money_received


machine_on = True

while machine_on:
    # Ask user for command or drink of choice
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'report':
        # print report of current reserves
        print(f"Water: {water_reserve}ml\n"
              f"Milk: {milk_reserve}ml\n"
              f"Coffee: {coffee_reserve}g\n"
              f"Money: ${profit}")

    elif user_choice == 'off':
        # turn off the machine
        machine_on = False

    # make coffee and/or execute command
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        # add coffee choice to a list of [cost, water, coffee, milk]
        coffee_choice = coffee_cost(user_choice)
        coffee_price = coffee_choice[0]
        coffee_water = coffee_choice[1]
        coffee_grounds = coffee_choice[2]
        coffee_milk = coffee_choice[3]

        # check the reserves
        if water_reserve < coffee_water:
            print("Sorry there is not enough water.")
        elif coffee_reserve < coffee_grounds:
            print("Sorry there is not enough coffee grounds.")
        elif milk_reserve < coffee_milk:
            print("Sorry there is not enough milk.")
        else:
            water_reserve -= coffee_water
            coffee_reserve -= coffee_grounds
            milk_reserve -= coffee_milk

            # ask for money entered and add it up
            money_received_total = calculate_money()
            # check if there was enough money entered
            if money_received_total > coffee_price:
                change = round(money_received_total - coffee_price, 2)
                profit += round(money_received_total - change, 2)

                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice}. Enjoy")
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Option not found. Please try again")
