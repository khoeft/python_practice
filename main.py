from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    options = menu.get_items()
    user_order = input(f'What would you like to order? {options} ')
    if user_order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_order == 'off':
        machine_on = False
        print('Goodbye')
    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)