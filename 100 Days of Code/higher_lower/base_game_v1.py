# from art import hilo
# from art import vs
from game_data import data
from random import randint
import os


def new_option(o):
    global list_2
    global list_1
    if o == 1:
        list_2 = list(data[randint(0, len(data) - 1)].values())
        return list_2
    elif o == 0:
        list_1 = list(data[randint(0, len(data) - 1)].values())
        return list_1


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


loop1 = True
score = 0
num1 = randint(0, len(data) - 1)
num2 = randint(0, len(data) - 1)
list_1 = list(data[num1].values())
list_2 = list(data[num2].values())

while loop1:

    A = list_1[1]
    B = list_2[1]
    # print(hilo)
    print(f"\nA: {list_1[0]}, a {list_1[2]}, from {list_1[3]}.")
    # print(vs)
    print(f"\n\nB: {list_2[0]}, a {list_2[2]}, from {list_2[3]}.")
    print(f"\nCurrent score: {score}")
    # print(list_1[1])
    # print(list_2[1])

    x = input("\nA or B?: ").lower()
    if x == 'b':
        if A <= B:
            list_2 = new_option(1)
            num2 = list_2[1]
            score += 1
            # print(f"\nCorrect!, current score: {score}")
            clear()
        elif A > B:
            print(f"\nIncorrect, you lose. Final score: {score}.")
            loop1 = False
    elif x == 'a':
        if B <= A:
            list_1 = new_option(0)
            num1 = list_1[1]
            score += 1
            # print(f"\nCorrect!, current score: {score}")
            clear()
        elif B > A:
            print(f"\nIncorrect, you lose. Final score: {score}.")
            loop1 = False
    else:
        print("\nChoose only 'a' or 'b'")
