
#------------------------------------------------------------#
Question-73:
Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.

Input:
[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

Output:
specified key:
[18, 22, 20, 18]

Hints:


Solution:
data=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

def convert_list_dict(data):
    lst=[]
    for i in range(len(data)):
        lst.append((data[i]['age']))
    print(lst)
convert_list_dict(data)

#------------------------------------------------------------#


