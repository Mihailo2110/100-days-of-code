# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "False input"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("What is your first name?: "),
#                   input("What is your last name?: ")))

# ---------------------------------------------------------
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 # print("Leap year.")
#                 return True
#             else:
#                 # print("Not leap year.")
#                 return False
#         else:
#             # print("Leap year.")
#             return True
#     else:
#         # print("Not leap year.")
#         return False
#
#
# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid input!"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True:
#         month_days[1] += 1
#     return month_days[month-1]
#
#
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# is_leap(year)
# days = days_in_month(year, month)
# print(days)
# --------------------------------------------------------------------------------------
print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    continue_calculating = True
    num1 = float(input("Whats the first number?: "))
    while continue_calculating:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        again = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

        if again == "y":
            continue_calculating = True
            num1 = answer
        elif again == "n":
            continue_calculating = False
            calculator()
        else:
            continue_calculating = True
            print("Wrong input, try again!")

calculator()

