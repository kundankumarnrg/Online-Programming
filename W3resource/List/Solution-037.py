
'''
#------------------------------------------------------------#
Question-37:
Write a Python program to find common items in two lists.

Input:
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]

Output:
res=[4, 5]

Hints:


Solution:
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]

#Type-1:------------------------------------#
def find_common_ele(lst1,lst2):
    res=[val for val in lst1 if val in lst2]
    print(res)
find_common_ele(lst1,lst2)


#Type-2:------------------------------------#
def find_commom_element(lst1,lst2):
    lst=[]
    for val in lst1:
        if val in lst2:
            lst.append(val)
    print(lst)
find_commom_element(lst1,lst2)


#Type-3:------------------------------------#
def find_common_ele(lst1,lst2):
    lst3=list(set(lst1) & set(lst2))
    print(lst3)

find_common_ele(lst1,lst2)

#------------------------------------------------------------#
'''

