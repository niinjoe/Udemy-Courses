from art import hilo
from art import vs
from game_data import data
from random import randint

def new_option():
    global list_2
    list_2 = list(data[randint(0, len(data) - 1)].values())
    return list_2

loop1 = True
score = 0

num1 = randint(0, len(data) - 1)
num2 = randint(0, len(data) - 1)
list_1 = list(data[num1].values())
list_2 = list(data[num2].values())

while loop1:

    A = list_1[1]
    B = list_2[1]
    print(f"A: {list_1[0]}, a {list_1[2]}, from {list_1[3]}.")
    print(f"B: {list_2[0]}, a {list_2[2]}, from {list_2[3]}.")
    # print(list_1[1])
    # print(list_2[1])
    
    x = input("A or B?: ").lower()
    if x == 'a':    
        if A >= B:
            list_2 = new_option()
            num2 = list_2[1]
            score += 1
            print(f"Correct!, current score: {score}")
        elif A < B:
            print(f"Incorrect, you lose. Final score: {score}.")
            loop1 = False
    elif x == 'b':    
        if B >= A:
            num1 = num2
            list_1 = list_2
            list_2 = new_option()
            num2 = list_1[1]
            score += 1
            
        elif B < A:
            print(f"Incorrect, you lose. Final score: {score}.")
            loop1 = False    
    else:
        print("Choose only 'a' or 'b'")






