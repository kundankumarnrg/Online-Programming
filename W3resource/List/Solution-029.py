'''
#------------------------------------------------------------#
Question-29:
Write a Python program to get unique values from a list.

Input:
[1,2,5,4,1,2,5,6,3,2,5,6,3]
[10, 20, 30, 40, 20, 50, 60, 40]

Output:
[1, 2, 3, 4, 5, 6]
[40, 10, 50, 20, 60, 30]

Hints:


Solution:
def unique_val_list(lst):
    print(lst)
    lst=list(set(lst))
    print(lst)
unique_val_list([1,2,5,4,1,2,5,6,3,2,5,6,3])
unique_val_list([10, 20, 30, 40, 20, 50, 60, 40])


#------------------------------------------------------------#
'''

