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
    "water": 200,
    "milk": 200,
    "coffee": 100
}
money = {
    "money": 2.50
}


def report():
    """Prints current resources and money level in coffee machine"""
    for item in resources:
        print(f'{item}: {resources[item]} ml')
    for item in money:
        print(f'{item}: ${money[item]}')


# accessing sub dictionaries = MENU['espresso']['ingredients']['water']

def check_resources(user_input):
    """Determines if the inputted product can be made with current resource and money level"""
    if user_input == 'espresso':
        can_make = False
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                if money['money'] >= MENU['espresso']['cost']:
                    can_make = True
                else:
                    can_make = False
                    print('Sorry, not enough money.')
            else:
                can_make = False
                print('Sorry, not enough coffee.')
        else:
            can_make = False
            print('Sorry, not enough water.')
    if user_input == 'latte':
        can_make = False
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                    if money['money'] >= MENU['latte']['cost']:
                        can_make = True
                    else:
                        can_make = False
                        print('Sorry, not enough money.')
                else:
                    can_make = False
                    print('Sorry, not enough coffee.')
            else:
                can_make = False
                print('Sorry, not enough milk.')
        else:
            can_make = False
            print('Sorry, not enough water.')
    if user_input == 'cappaccino':
        can_make = False
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                    if money['money'] >= MENU['cappuccino']['cost']:
                        can_make = True
                    else:
                        can_make = False
                        print('Sorry, not enough money.')
                else:
                    can_make = False
                    print('Sorry, not enough coffee.')
            else:
                can_make = False
                print('Sorry, not enough milk.')
        else:
            can_make = False
            print('Sorry, not enough water.')
    return can_make


def add_ingredients():
    """Adds 100ml to each resource level"""
    resources['water'] = resources['water'] + 100
    resources['milk'] = resources['milk'] + 100
    resources['coffee'] = resources['coffee'] + 100


def add_money():
    """Allows user to input how much money (in change) that they want to add to the coffee machine"""
    num_quarters = int(input('How many quarters would you like to input?: '))
    num_dimes = int(input('How many dimes would you like to input?: '))
    num_nickels = int(input('How many nickels would you like to input?: '))
    num_pennies = int(input('How many pennies would you like to input?: '))
    quarters = num_quarters * .25
    dimes = num_dimes * .10
    nickels = num_nickels * .05
    pennies = num_pennies * .01
    money['money'] = money['money'] + quarters + dimes + nickels + pennies


coffee_machine = True
while coffee_machine:
    user_input = input(
        "What would you like? Type 'espresso', 'latte', or 'cappaccino'. \nType 'report' to see ingredients level. "
        "\nType 'add ingredients' to add ingredients or type 'add money' to add money. \nType 'off' to turn coffee "
        "machine off. ")
    if user_input == 'report':
        report()
    elif user_input == 'add ingredients':
        add_ingredients()
        print('Ingredients have been added.')
    elif user_input == 'off':
        coffee_machine = False
        print('Thank you. Goodbye.')
    elif user_input == 'add money':
        add_money()
    elif user_input == 'espresso':
        resources_available = check_resources(user_input)
        if resources_available:
            resources['water'] -= MENU['espresso']['ingredients']['water']
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            money['money'] -= MENU['espresso']['cost']
            print(f'Here is your {user_input}! Enjoy!')
        else:
            print('Please add ingredients.')
    elif user_input == 'latte':
        resources_available = check_resources(user_input)
        if resources_available:
            resources['water'] -= MENU['latte']['ingredients']['water']
            resources['milk'] -= MENU['latte']['ingredients']['milk']
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            money['money'] -= MENU['latte']['cost']
            print(f'Here is your {user_input}! Enjoy!')
        else:
            print('Please add ingredients.')
    elif user_input == 'cappaccino':
        resources_available = check_resources(user_input)
        if resources_available:
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            money['money'] -= MENU['cappuccino']['cost']
            print(f'Here is your {user_input}! Enjoy!')
        else:
            print('Please add ingredients.')
