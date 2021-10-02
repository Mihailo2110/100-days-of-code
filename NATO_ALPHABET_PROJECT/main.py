import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}

run = True

while run:
    try:
        word = input("Enter a word: ").upper()
        letter_list = [new_dict[letter] for letter in word]
        run = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(letter_list)

