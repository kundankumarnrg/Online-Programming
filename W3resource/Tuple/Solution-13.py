'''
#------------------------------------------------------------#
Question-13:
Write a Python program to slice a tuple

Input:
(1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 3, 2, 5, 8)

Output:
After slicing:
(1, 2, 3, 4, 5)
(7, 8, 9, 6, 3, 2, 5, 8)
(8, 9, 6, 3, 2, 5, 8)


Hints:


Solution:
t=1,2,3,4,5,6,7,8,9,6,3,2,5,8

def slicing_tuple(t):
    print(t)
    print("After slicing:")
    sli_val1=t[:5]
    sli_val2=t[6:]
    sli_val3=t[-7:]
    print(sli_val1)
    print(sli_val2)
    print(sli_val3)

slicing_tuple(t)

#------------------------------------------------------------#
'''

