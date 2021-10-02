# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
#
# student_grades = {}
#
# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"
#
#
# print(student_grades)

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# ----------------------------------------------------------------------------------------
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"],
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"],
#     }
# ]
#
#
# def add_new_country(country_visited, times_visited, cities_visited):
#     travel_log.append({
#         "country": country_visited,
#         "visits": times_visited,
#         "cities": cities_visited
#     })
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)




print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
''')
print("Welcome to the secret auction program!")
bidders = True
recnik = {}
vrednosti = []


while bidders is True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?:$ "))
    recnik[name] = bid
    more_bidders = input("Are there any more bidders? Type 'y' or 'n'.")
    if more_bidders == "n":
        bidders = False
    elif more_bidders == "y":
        bidders = True
    else:
        bidders = False
        print("Wrong input!")
        exit(1)

max_value = max(recnik.values())

for key, value in recnik.items():
    if max_value == value:
        winner = key

print(f"The winner is {winner} with the bid {max_value}")
