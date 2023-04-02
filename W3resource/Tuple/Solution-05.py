'''
#------------------------------------------------------------#
Question-5:
Write a Python program to add an item to a tuple.

Input:
t = (4, 6, 2, 8, 3, 1) 

Output:
(4, 6, 2, 8, 3, 1, 100)

Hints:


Solution:
t = (4, 6, 2, 8, 3, 1) 

def add_ele_tuple(t):
    print(t)
    lst=list(t)
    lst.append(100)
    print(tuple(lst))
add_ele_tuple(t)


#------------------------------------------------------------#
'''

