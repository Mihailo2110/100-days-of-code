# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user = []
# computer = []
# def deal():
#     user.append(random.choice(cards))
#     user.append(random.choice(cards))
#     computer.append((random.choice(cards)))
#     computer.append((random.choice(cards)))
#     return f"You got {user}\n" \
#            f"computer's first card is {computer[0]}"
#
# def is_blackjack():
#     if sum(user) == 21:
#         print("Blackjack! You won!")
#         exit(1)
#     elif sum(computer) == 21:
#         print("Blackjack! You loose!")
#         exit(2)
#
# def is_user_over_21():
#     if sum(user) >= 21:
#         if 11 in user:
#             user.pop()
#             user.append(1)
#             return user
#
# def is_computer_over_21():
#     if sum(computer) >= 21:
#         if 11 in computer:
#             computer.pop()
#             computer.append(1)
#             return computer
#
# def another_card():
#     answer = input("Do you want another card?: ")
#     if answer == "yes":
#         user.append(random.choice(cards))
#         if sum(user) == 21:
#             print("Blackjack! You won!")
#             exit(3)
#         elif sum(user) > 21:
#             print("You loose!")
#             exit(4)
#         else:
#             while sum(computer) < 17:
#                 computer.append(random.choice(cards))
#                 if sum(computer) == 21:
#                     print("Blackjack! You loose!")
#                     exit(5)
#                 elif sum(computer) > 21:
# #                     print("You win!")
# #                     exit(6)
#

#
# #
# def score():
#     if 21 >= sum(user) > sum(computer):
#         return "User wins!"
#     elif 21 >= sum(computer) > sum(user):
#         return "Computer wins!"
#     elif 21 >= sum(user) == sum(computer):
#         return "Draw!"

import random

cards = [11, 2, 3, 4, 5] #, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []

def blackjack():
    start = input("Do you wanna play blackjack?: ")
    if start == "y":
        print("""
        .------.            _     _            _    _            _
        |A_  _ |.          | |   | |          | |  (_)          | |
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |
              `------'                           |__/
        """
              )

        user.append(random.choice(cards))
        user.append(random.choice(cards))
        computer.append((random.choice(cards)))
        computer.append((random.choice(cards)))
        print(f"You got {user}\n"
              f"computer's first card is {computer[0]}")

        if sum(user) == 21 and sum(computer) < 21:
            print(f"You got {sum(user)}\n"
                  f"Computer got {sum(computer)}\n"
                  f"Blackjack! You win!")
            exit(1)
        elif sum(user) == 21 and sum(computer) < 21:
            print(f"You got {user} = {sum(user)}\n"
                  f"Computer got {computer} = {sum(computer)}\n"
                  f"Draw!")

        answer = input("Do you want another card?: ")
        while answer == "y":
            user.append(random.choice(cards))
            print(user)
            if sum(user) == 21:
                print(f"You got {user} = {sum(user)}\n"
                      f"Computer got {computer} = {sum(computer)}\n"
                      f"Blackjack! You win!")

                exit(2)
            elif sum(user) > 21:
                if 11 in user:
                    user.remove(11)
                    user.append(1)
                    continue
                else:
                    print(f"You got {user} = {sum(user)}\n"
                          f"Computer got {computer} = {sum(computer)}\n"
                          f"You loose!")
                    exit(3)
            else:
                answer = input("Do you want another card?: ")

        if answer == "n":
            while sum(computer) < 17:
                computer.append(random.choice(cards))
                print(computer)
                if sum(computer) == 21:
                    print(f"You got {user} = {sum(user)}\n"
                          f"Computer got {computer} = {sum(computer)}\n"
                          f"You loose!")
                    exit(4)
                elif sum(computer) > 21:
                    if 11 in computer:
                        computer.remove(11)
                        computer.append(1)
                    else:
                        print(f"You got {user} = {sum(user)}\n"
                              f"Computer got {computer} = {sum(computer)}\n"
                              f"You win!")
                        exit(5)

        if 21 >= sum(user) > sum(computer):
            print(f"You got {user} = {sum(user)}\n"
                  f"Computer got {computer} = {sum(computer)}\n"
                  f"You win!")
            exit(6)
        elif 21 >= sum(computer) > sum(user):
            print(f"You got {user} = {sum(user)}\n"
                  f"Computer got {computer} = {sum(computer)}\n"
                  f"You loose!")
            exit(7)
        elif 21 >= sum(user) == sum(computer):
            print(f"You got {user} = {sum(user)}\n"
                  f"Computer got {computer} = {sum(computer)}\n"
                  f"Draw!")
            exit(8)
    else:
        exit(9)

blackjack()
