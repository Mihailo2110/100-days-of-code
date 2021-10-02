from random import randint
print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")

game = input(f"Welcome to the Number Guessing Game!\n"
             f"I'm thinking of a number between 1 and 100\n"
             f"Choose a difficulty. Type 'easy' or 'hard': ")
guess_count = 0

guessing_number = randint(1, 100)
# print(guessing_number)

if game == "easy":
    guess_count += 10
    print(f"You have {guess_count} attempts remaining to guess the number.")

elif game == "hard":
    guess_count += 5
    print(f"You have {guess_count} attempts remaining to guess the number.")

while guess_count > 0:
    guess = int(input("Make a guess: "))
    guess_count -= 1
    if guess == guessing_number:
        print("Great, you got it!")
        break
    elif guess < guessing_number:
        print(f"Too low!\n"
              f"Guess again!")
    else:
        print(f"Too high!\n"
              f"Guess again!")
    print(f"You have {guess_count} attempts remaining to guess the number.")
else:
    print("You loose!")
    exit(1)
