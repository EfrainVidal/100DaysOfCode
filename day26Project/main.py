
#                        List Comprehension
numbers = [1, 2, 3]
# new form of a for loop
# new_numbers = [new_item for item in list]
new_number = [n + 1 for n in numbers]

name = "Efrain"
# new_list = [letter for letter in name]
letter_list = [letter for letter in name]

range(1, 5)
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

#                       Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [n for n in names if len(n) < 5]

long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)

#                        Dictionary Comprehension
# new_dict ={new_key:new_value for item in list}
# new_dict ={new_key:new_value for (key,value) in dict.items()}
# new_dict ={new_key:new_value for (key,value) in dict.items() if test}


import random
import pandas
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_score = {student:random.randint(1, 100) for student in names}


passed_students = {student:grade for (student, grade) in students_score.items() if grade >= 60}
print(passed_students)

scores = {"Alex":36, "Beth":65, "Caroline":95, "Dave":75, "Eleanor":96, "Freddie":100}

student_data_frame = pandas.DataFrame(scores)
print(student_data_frame)

#                       Loop though a data frame
# for (key, value) in student_data_frame.items():
#   print(value)

#                       Loop though rows in a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)