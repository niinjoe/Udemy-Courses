import random
import os
from art import guess_number

num_list = list(range(1, 101))
chosen_num = random.choice(num_list)
turns = 0

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def difficulty(x):
  global turns
  if x == 'e':
    turns = 10
  elif x == 'h':
    turns = 5

def play():
  print(guess_number)
  global turns
  loop = True
  difficulty(input("Select difficulty: 'e' for Easy or 'h' for Hard: "))
  while loop:
    guess = int(input("Guess number from 1 to 100: "))
    if turns == 1:
      print(f"You ran out of turns.\n'{chosen_num}' was the chosen number.\nGame over.")
      loop = False
    elif guess > chosen_num:
      turns -= 1
      print(f"Too High.\nYou have {turns} attempts left.")
    elif guess < chosen_num:  
      turns -= 1
      print(f"Too Low.\nYou have {turns} attempts left.")
    else:
      print(f"You guessed it with {turns} attempts left!\n{chosen_num} was the chosen number. ")
      loop = False

play()
if input("Play again? 'y'/'n': ") == 'y':
  clear()
  play()
else:
  clear()