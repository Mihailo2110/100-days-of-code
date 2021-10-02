from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]

    password = password_symbols+password_letters+password_numbers
    shuffle(password)
    password = "".join(password)
    input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No data file found.")
    else:
        if input_web.get() in data:
            messagebox.showinfo(title=f"{input_web.get()}", message=f"Email: {data[input_web.get()]['email']} \nPassword: {data[input_web.get()]['password']}")
        else:
            messagebox.showinfo(title=f"{input_web.get()}", message=f"No data for {input_web.get()} found!")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    new_data = {input_web.get():{
            "email": input_em.get(),
            "password": input_pass.get(),
    }}

    if len(input_web.get()) == 0 or len(input_pass.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left ay fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            input_web.delete(0, END)
            input_pass.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)

email_label = Label(text = "Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text = "Password:")
password_label.grid(column=0, row=3)

input_web = Entry(width = 26)
input_web.grid(column=1, row=1)
input_web.focus()

input_em = Entry(width = 45)
input_em.grid(column=1, row=2, columnspan=2)
input_em.insert(0, "mihailomilovanovic21@gmail.com")

input_pass = Entry(width = 26)
input_pass.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", width = 15, command = generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width = 40, command=add)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width = 15, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()