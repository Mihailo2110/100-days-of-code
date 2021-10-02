import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for i in range(nr_letters)]
password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
password = password_symbols+password_letters+password_numbers

# password = []
#
# for i in range(1, nr_letters + 1):
#     password.append(random.choice(letters))
#
# for i in range(1, nr_numbers + 1):
#     password.append(random.choice(numbers))
#
# for i in range(1, nr_symbols + 1):
#     password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)

password1 = ""
for i in password:
    password1 += i

print(f"Your password is {password1}")

