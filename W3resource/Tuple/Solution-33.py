'''
#------------------------------------------------------------#
Question-:
Write a Python program to convert a given list of tuples to a list of lists.

Input:
tuples= [(1, 2), (2, 3), (3, 4)]
tuples1= [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

Output:
 [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

Hints:


Solution:
def convert_list_tuple(t):
    print(t)
    print("After convertion:")
    lst=[]
    for val in t:
        l=list(val)
        lst.append(l)
    return lst
print(convert_list_tuple(t= [(1, 2), (2, 3), (3, 4)]))
print(convert_list_tuple(t=[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]))

#------------------------------------------------------------#
'''


