'''
#------------------------------------------------------------#
Question-21:
Write a Python program to replace the last value of tuples in a list.

Input:
lst=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

Output:
[(10, 20, 100), (40, 50, 100), (70, 80, 100)]

Hints:


Solution:
lst=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

def replace_last_ele(lst):
    lst1=[]
    for val in lst:
        l=list(val)
        l.pop()
        l.append(100)
        t1=tuple(l)
        lst1.append(t1)
    print(lst1)

replace_last_ele(lst)

#------------------------------------------------------------#
'''

