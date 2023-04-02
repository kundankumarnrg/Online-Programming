'''
#------------------------------------------------------------#
Question-12:
Write a Python program to remove an item from a tuple.

Input:
(10, 20, 30, 40, 50)

Output:
(20, 30, 40, 50)

Hints:


Solution:
t=10,20,30,40,50

def remove_ele(t):
    print(t)
    lst=list(t)
    lst.remove(10)
    t1=tuple(lst)
    print(t1)
remove_ele(t)

#------------------------------------------------------------#
'''

