import random
import os
from art import blackjack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
comp_hand = []
loop1 = True

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
def another():
    k = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if k == 'y':
        clear()
        user_hand.clear()
        comp_hand.clear()
        return True
    elif k == 'n':
        return False
    else:
        print("Only type 'y' or 'n' to continue.")
def deal_card():
    return random.choice(cards)
def add_card(x):
    if x == "user":
        return user_hand.append(deal_card())
    elif x == "cpu":
        return comp_hand.append(deal_card())
def calculate_score(y):
    if y == "user":
        return sum(user_hand)
    elif y == "cpu":
        return sum(comp_hand)
def ace(z):
    if z == "user":
        user_hand.remove(11)
        user_hand.append(1)
    elif z == "cpu":
        comp_hand.remove(11)
        comp_hand.append(1)
def check_ace(c):
    if c == 'user':
        for card in user_hand:
            if calculate_score('user') < 22:
                break
            elif card == 11:
                ace('user')
    elif c == 'cpu':
        for card in comp_hand:
            if calculate_score('cpu') < 22:
                break
            elif card == 11:
                ace('cpu')
def blackjack(a):
    if a == 'cpu':
        return 1
    elif a == 'user':
        return 0
def result(win_condition):
    if win_condition == 4:
        return f"\n\nYou win!\nYour hand: {user_hand}, total score: {calculate_score('user')}\nComputer's hand: {comp_hand}, computer's total score {calculate_score(y = 'cpu')}"
    elif win_condition == 2:
        return f"\n\nDraw!\nYour hand: {user_hand}, total score: {calculate_score('user')}\nComputer's hand: {comp_hand}, computer's total score {calculate_score(y = 'cpu')}"
    elif win_condition == 3:
        return f"\n\nYou lose!\nYour hand: {user_hand}, total score: {calculate_score('user')}\nComputer's hand: {comp_hand}, computer's total score {calculate_score(y = 'cpu')}"
    elif win_condition == 1:
        return f"\n\nComputer got Blackjack, you lose!\nYour hand: {user_hand}, total score: {calculate_score('user')}\nComputer's hand: {comp_hand}, computer's total score {calculate_score(y = 'cpu')}"
    elif win_condition == 0:
        return f"\n\nYou got Blackjack, you win!\nYour hand: {user_hand}, total score: {calculate_score('user')}\nComputer's hand: {comp_hand}, computer's total score {calculate_score(y = 'cpu')}"



while loop1:
    loop2 = True
    loop3 = True
    loop4 = True
    print(blackjack)
    y = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if y == "y":
        for card in range(2):
            add_card("user")
            add_card("cpu")
        check_ace('user')
        check_ace('cpu')
        if calculate_score('cpu') == 21:
            print(result(blackjack('cpu')))
            loop2 = False
            loop4 = False
        elif calculate_score('user') == 21:
            print(result(blackjack('user')))
            loop2 = False
            loop4 = False
        while loop2:
            print(f"This is your hand: {user_hand}, total score: {calculate_score('user')}.\nThis is the computer's first card: {comp_hand[0]}.")
            draw_again = input("Type 'y' to draw another card or 'n' to pass: ").lower()
            if draw_again == 'n':
                loop2 = False
            elif draw_again == 'y':
                add_card('user')
            else:
                print("Only type 'y' or 'n' to continue.")
            check_ace('user')
            if calculate_score('user') >= 21:
                loop2 = False
        while loop4:
            if calculate_score('user') > 21:
                loop4 = False
            elif calculate_score('cpu') < calculate_score('user'):
                while loop3:
                    if calculate_score('cpu') > 18:
                        loop3 = False
                        loop4 = False
                    elif calculate_score('cpu') < 22:
                        add_card('cpu')
                    check_ace('cpu')
                    if calculate_score('cpu') > 21:
                        loop3 = False
                        loop4 = False
            else:
                loop3 = False
                loop4 = False
            if calculate_score('user') >= 22:
                print(result(3))
                loop2 = False
            elif calculate_score('cpu') >= 22:
                print(result(4))
                loop2 = False
            elif calculate_score('cpu') < calculate_score('user'):
                print(result(4))
                loop2 = False
            elif calculate_score('user') < calculate_score('cpu'):
                print(result(3))
                loop2 = False
            elif calculate_score('cpu') == calculate_score('user'):
                print(result(2))
                loop2 = False
    elif y == 'n':
        loop1 = False
    else:
        print("Only type 'y' or 'n' to continue.")   
    loop1 = another()