import pandas



student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

{new_key:new_value for (index, row) in student_data_frame.itterows()}