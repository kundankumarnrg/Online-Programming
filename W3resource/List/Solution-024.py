'''
#------------------------------------------------------------#
Question-24:
Write a Python program to append a list to the second list. 

Input:
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']

Output:
res=[1, 2, 3, 0, 'Red', 'Green', 'Black']

Hints:


Solution:
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']

#Type-1:----------------------------------------#
def append_listval_into_secondlist(list1,list2):
    for val in list2:
        list1.append(val)
    print(list1)
append_listval_into_secondlist(list1,list2)

#Type-2:----------------------------------------#
def append_listval_into_secondlist(list1,list2):
    return list1+list2
print(append_listval_into_secondlist(list1,list2))



#------------------------------------------------------------#
'''




