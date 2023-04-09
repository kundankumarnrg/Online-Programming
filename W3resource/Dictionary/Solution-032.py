
#------------------------------------------------------------#
Question32-:
Write a Python program to print a dictionary line by line.

Input:
students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}

Output:
Aex
class : V
rolld_id : 2
Puja
class : V
roll_id : 3

Hints:


Solution:
students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}

def print_data_line_by_line(students):
    for value in students:
        print(value)
        for val in students[value]:
            print(val,":",students[value][val])

print_data_line_by_line(students)

#------------------------------------------------------------#


