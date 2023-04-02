'''
#------------------------------------------------------------#
Question-11:
Write a Python function that takes two lists and returns True if they have at least one common member.

Input:
lst1=[1,2,3,4,5]
lst2=[7,8,9,5,6]

lst1=[1,2,3,4,5]
lst2=[9,8,7,6]

Output:
True
False

Hints:


Solution:
lst1=[1,2,3,4,5]
lst2=[7,8,9,5,6]
#lst2=[9,8,7,6]

def find_commom_element(lst1,lst2):
    for val in lst1:
        if val in lst2:
            tem=True
            break
        else:
            tem=False
    return tem
res=find_commom_element(lst1,lst2)
print(res)

#------------------------------------------------------------#
'''
