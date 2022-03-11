import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
comp_hand = [11, 10, 2]
loop1 = True
loop2 = True
loop3 = True

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
def blackjack(a):
    if a == 'cpu':
        return 1
    elif a == 'user':
        return 0
def draw(b):
    if b == 'user':
        add_card("user")
    elif b == 'cpu':
        add_card('cpu')

while loop3:
    if calculate_score('cpu') > 21:
        for card in comp_hand:
            if card == 11:
                ace('cpu')
    if calculate_score('cpu') > 15:
        loop3 = False
    elif calculate_score('cpu') < 21:
        draw('cpu')
    elif calculate_score('cpu') > 21:
        loop3 = False