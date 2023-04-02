

'''
#------------------------------------------------------------#
Question-14:
Write a Python program to print the numbers of a specified list after removing even numbers from it.

Input:
lst=[7,8, 120, 25, 44, 20, 27]

Output:
res=[7, 25, 27]

Hints:


Solution:
lst=[7,8, 120, 25, 44, 20, 27]
def remove_even_ele(lst):
    print(lst)
    lst1=[]
    for val in lst:
        if val%2!=0:
            lst1.append(val)
    print(lst1)
remove_even_ele(lst)

def remove_even_element(lst):
    print(lst)
    res=[val for val in lst if val%2!=0]
    print(res)
remove_even_element(lst)

#------------------------------------------------------------#
'''



