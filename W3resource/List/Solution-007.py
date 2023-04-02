


'''
#------------------------------------------------------------#
Question-7:
Write a Python program to remove duplicates from a list.

input:
lst=[1,2,5,8,9,6,5,4,1,2,3,6,5,8]


output:
res=[1, 2, 5, 8, 9, 6, 4, 3]

Hints:


Solution:
lst=[1,2,5,8,9,6,5,4,1,2,3,6,5,8]
#Type-6:--------------------------------#

def remove_duplicate(lst):
    print(lst)
    lst1=list(set(lst))
    print(lst1)
remove_duplicate(lst)


#Type-2:--------------------------------#
def remove_duplicate_val(lst):
    print(lst)
    lst1=[]
    for val in lst:
        if val not in lst1:
            lst1.append(val)
    print(lst1)
remove_duplicate_val(lst)
#------------------------------------------------------------#
'''



