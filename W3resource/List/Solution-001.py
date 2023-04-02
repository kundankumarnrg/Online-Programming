'''
#------------------------------------------------------------#
Question-1:
Write a Python program to sum all the items in a list.

input:
lst=[-1,2,3,4,5,6]

output:
Sum of list element:  19

Hints:


Solution:
lst=[-1,2,3,4,5,6]
def sum_all_element(lst):
    sum=0
    for val in lst:
        sum=sum+val
    return sum    
    
res=sum_all_element(lst)
print("Sum of list element: ",res)

#------------------------------------------------------------#
'''













