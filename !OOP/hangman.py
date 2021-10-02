# import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = input("Unesite rec: ")
# chosen_word = random.choice(word_list)

lives = 6

# print(f"chosen word is {chosen_word}")

display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)
print(stages[6])

guesses = []

while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You have allready guessed that letter!")
        continue
    guesses.append(guess)
    if guess not in chosen_word:
        if lives > 1:
            lives -= 1
            print(lives)
            if lives == 5:
                print(stages[5])
            elif lives == 4:
                print(stages[4])
            elif lives == 3:
                print(stages[3])
            elif lives == 2:
                print(stages[2])
            elif lives == 1:
                print(stages[1])
                print('One mistake left!!')
        else:
            print(stages[0])
            print("you loose!")
            exit(1)
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
else:
    print("you win!")
    exit(2)










