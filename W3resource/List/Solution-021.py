'''
#------------------------------------------------------------#
Question-21:
Write a Python program to convert a list of characters into a string.

Input:
lst=['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', 'l', 'a', 'n', 'g']

Output:
res=python program lang

Hints:


Solution:
lst=['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', 'l', 'a', 'n', 'g']

#Type-1:----------------------------------#
def list_string_formate(lst):
    print(lst)
    print(''.join(lst))
list_string_formate(lst)

#Type-2:----------------------------------#
def list_string_format(lst):
    str1=""
    print(lst)
    for ch in lst:
        str1=str1+ch
    print(str1)
list_string_format(lst)

#------------------------------------------------------------#
'''





