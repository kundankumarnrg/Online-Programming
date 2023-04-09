
#------------------------------------------------------------#
Question-33:
Write a Python program to check if multiple keys exist in a dictionary.

Input:
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

Output:
Aex
class : V
rolld_id : 2
Puja
class : V
roll_id : 3

Hints:


Solution:
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

def check_multiple_keys_exist(student,keys):
    lst=list(student)
    c=0
    for v in keys:
        if v in lst:
            c=c+1
    print("True" if(len(keys)==c) else "False")

check_multiple_keys_exist(student,keys={'class', 'name'})
check_multiple_keys_exist(student,keys={'name', 'Alex'})
check_multiple_keys_exist(student,keys={'roll_id', 'name'})

#------------------------------------------------------------#


