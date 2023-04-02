'''
#------------------------------------------------------------#
Question-50:
Write a Python program to sort a list of nested dictionaries.

Input:
[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]     

Output:
Sorted List:                                                                                                  
[{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]  

Hints:


Solution:
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

def sorted_nested_list(my_list):
    print(my_list)
    my_list.sort(key=lambda val: val['key']['subkey'],reverse=True)
    print(my_list)
sorted_nested_list(my_list)

#------------------------------------------------------------#
'''

