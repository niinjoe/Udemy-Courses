from lib import MENU, resources
import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def inventory(var):
    if (
        resources["water"] - MENU[var]["ingredients"]["water"] < 0
        or resources["coffee"] - MENU[var]["ingredients"]["coffee"] < 0
        or resources["milk"] - MENU[var]["ingredients"]["milk"] < 0
    ):
        return False


def consume(var):
    if X == True:
        resources["water"] -= MENU[var]["ingredients"]["water"]
        resources["coffee"] -= MENU[var]["ingredients"]["coffee"]
        resources["milk"] -= MENU[var]["ingredients"]["milk"]
        return True


def money(var):
    global caja, CASH
    total = sum(CASH)
    if total >= MENU[var]["cost"]:
        caja += float(MENU[var]["cost"])
        change = total - MENU[var]["cost"]
        print(f"\n\tYour coffee is ready.\n\tThis is your change ${change:.2f}.")
        return True
    else:
        print(
            f"Insufficient funds, please try again.\n\t\tHere's your refund of ${total:.2f}."
        )
        return False


def coins():
    print("Insert coins:")
    quarters = float(input("\tAmount of quarters: ")) * 0.25
    dimes = float(input("\tAmount of dimes: ")) * 0.1
    nickels = float(input("\tAmount of nickels: ")) * 0.05
    pennies = float(input("\tAmount of pennies: ")) * 0.01
    return [quarters, dimes, nickels, pennies]


loop1 = True
caja = 0
while loop1:
    clear()
    beverage = input(
        "What would you like?:\nEspresso (e) / Latte (l) / Cappuccino (c): "
    )
    if beverage == "report":
        print(
            f"This is the current inventory:\nWater: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}g.\nMoney: ${caja:.2f}."
        )
    elif beverage == "off":
        if input("Are you sure you want to TURN OFF the machine? y/n: ") == "y":
            break
        else:
            continue
    elif beverage == "e" or beverage == "c" or beverage == "l":
        if beverage == "e":
            cost = input(
                f"\tAn espresso costs ${MENU['espresso']['cost']}0.\n\tDo you want it? y/n: "
            )
            if cost == "y":
                if inventory("espresso") == False:
                    print("Not enough resources.")
                else:
                    CASH = coins()
                    X = money("espresso")
                    if X == True:
                        consume("espresso")
                        print("Enjoy!")
        elif beverage == "c":
            cost = input(
                f"\tA cappuccino costs ${MENU['cappuccino']['cost']}0.\n\tDo you want it? y/n: "
            )
            if cost == "y":
                if inventory("cappuccino") == False:
                    print("Not enough resources.")
                else:
                    CASH = coins()
                    X = money("cappuccino")
                    if X == True:
                        consume("cappuccino")
                        print("Enjoy!")
        elif beverage == "l":
            cost = input(
                f"\tA latte costs ${MENU['latte']['cost']}0.\n\tDo you want it? y/n: "
            )
            if cost == "y":
                if inventory("latte") == False:
                    print("Not enough resources.")
                else:
                    CASH = coins()
                    X = money("latte")
                    if X == True:
                        consume("latte")
                        print("Enjoy!")
    else:
        print(
            "Please select from the given options.\n\n\tFor technician: Type 'off' or 'report'..."
        )
    input("\n\tPress Enter to continue... ")
