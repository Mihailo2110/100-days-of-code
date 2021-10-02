from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    my_label_1.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=130, pady=80)

input = Entry(width = 10)
input.grid(column=1, row=0)

my_label = Label(text = "", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=0)

my_label = Label(text = "Miles", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=0)

my_label = Label(text = "is equal to", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=1)

my_label_1 = Label(text = 0, font=("Arial", 12, "bold"))
my_label_1.grid(column=1, row=1)

my_label = Label(text = "Km", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()