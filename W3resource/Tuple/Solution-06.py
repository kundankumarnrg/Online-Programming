'''
#------------------------------------------------------------#
Question-6:
Write a Python program to convert a tuple to a string.

Input:
t = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

Output:
exercises

Hints:


Solution:
t = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

#Type-1:-------------------------------------
def convert_tuple_string(t):
    print(t)
    res=""
    for ch in t:
        res=res+ch
    print(res)
convert_tuple_string(t)

#Type-2:------------------------------------
def convert_tuple_str(t):
    print(t)
    print(''.join(t))
convert_tuple_str(t)

#------------------------------------------------------------#
'''





