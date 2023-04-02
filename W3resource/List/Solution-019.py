'''
#------------------------------------------------------------#
Question-19:
Write a Python program to calculate the difference between the two lists.

Input:
lst1=[1, 3, 5, 7, 9]
lst2=[1, 2, 4, 6, 7, 8]

Output:
res=[3, 5, 9, 2, 4, 6, 8]
res=[9, 3, 5, 8, 2, 4, 6]

Hints:


Solution:
lst1=[1, 3, 5, 7, 9]
lst2=[1, 2, 4, 6, 7, 8]

#Type-1:-----------------------------------#
def calculate_difference(lst1,lst2):
    lst3=[]
    for val in lst1:
        if val not in lst2:
            lst3.append(val)
    for val in lst2:
        if val not in lst1:
            lst3.append(val)
    print(lst3)
calculate_difference(lst1,lst2)

#Type-2:-----------------------------------#
def difference_list(lst1,lst2):
    d1=list(set(lst1)-set(lst2))
    d2=list(set(lst2)-set(lst1))
    res=d1+d2
    print(res)
difference_list(lst1,lst2)

#------------------------------------------------------------#
'''



