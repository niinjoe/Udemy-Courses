from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mn = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

switch = True

while switch:
    user_input = input(f"What drink would you like to order? {mn.get_items()}: ")
    if user_input == 'off':
        input("Shutting down... Press Enter to continue")
        switch = False
    elif user_input == 'report':
        cm.report()
        mm.report()
    else:
        selected_drink = mn.find_drink(user_input)
        if cm.is_resource_sufficient(selected_drink) & mm.make_payment(selected_drink.cost):
            cm.make_coffee(selected_drink)
