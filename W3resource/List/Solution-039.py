'''
#------------------------------------------------------------#
Question-39:
Write a Python program to convert a list of multiple integers into a single integer.

Input:
lst=[11,33,50]

Output:
res=113350

Hints:


Solution:
lst=[11,33,50]

def multiple_int_into_single_int(lst):
    print(lst)
    str1=""
    for val in lst:
        str1=str1+str(val)
    print(int(str1))
multiple_int_into_single_int(lst)

#------------------------------------------------------------#
'''
