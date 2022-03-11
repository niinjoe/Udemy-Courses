from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    selection = input(f"Select a coffee: {menu.get_items()}: ")
    if selection == 'off':
        on = False
    elif selection == 'report':
        coffee.report()
        money.report()
    else:
        taza = menu.find_drink(selection)
        if coffee.is_resource_sufficient(taza) and money.make_payment(taza.cost):
            coffee.make_coffee(taza)

