'''
#------------------------------------------------------------#
Question-23:
Write a Python program to flatten a shallow list.

Input:
lst=[[1,2,3],[4,5,6],[7,8,9],[7,4,1]]

Output:
res=[1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 4, 1]

Hints:


Solution:
lst=[[1,2,3],[4,5,6],[7,8,9],[7,4,1]]

def flatten_shallow_list(lst):
    print(lst)
    new_list=[]
    for value in lst:
        for val in value:
            new_list.append(val)
    print(new_list)

flatten_shallow_list(lst)

#------------------------------------------------------------#
'''


