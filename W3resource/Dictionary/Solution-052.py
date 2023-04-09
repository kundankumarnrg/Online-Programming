
#------------------------------------------------------------#
Question52-:
Write a Python program to extract a list of values from a given list of dictionaries.

Input:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

Output:
Extract a list of values from said list of dictionaries where subject = Science
[92, 94, 88]

Extract a list of values from said list of dictionaries where subject = Math
[90, 89, 92]

Hints:


Solution:
lst=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

#Type-1:---------------------------------------------
def extract_list_values(lst):
    lst2=[]
    for value in lst:
        lst2.append(value['Science'])
    print(lst2)

extract_list_values(lst)

#Type-2:---------------------------------------------
def extract_list_values(lst):
    res=[val['Science'] for val in lst]
    print(res)

extract_list_values(lst)

#------------------------------------------------------------#





