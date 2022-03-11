import random

word_list = ["aardvark", "baboon", "camel"]

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
  display += "_"
print(f"Guess the word, it has {len(display)} blanks.")

vidas = 6
h=0

while "_" in display:
  
  guess = input("Guess a letter: ").lower()
  
  if guess.isalpha() == False:
    print("Solo puede utilizar letras.")
  
  if len(guess) > 1:
    print("ERROR: Solo puede ser una letra a la vez.")
  
  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = chosen_word[position]
  print(' '.join(display))

  if guess not in chosen_word:
    vidas -= 1
    print(hangman[h])
    h+=1
  
  if "_" not in display:
    print("Palabra completada. Ganaste!")
  
  if vidas < 1:
    print("Ya no te quedan mas intentos. Perdiste.")
    break