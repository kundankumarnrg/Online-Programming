'''
#------------------------------------------------------------#
Question-:
Write a Python program to convert a given tuple of positive integers into an integer.

Input:
(1, 2, 3)
(10, 20, 40, 5, 70)

Output:
123
102040570

Hints:


Solution:
#Type-1:---------------------------------------------------
def convert_tuple_possitive_integer(t):
    str1=""
    for val in t:
        str1=str1+str(val)
    return int(str1)

print(convert_tuple_possitive_integer(t=(1, 2, 3)))
print(convert_tuple_possitive_integer(t=(10, 20, 40, 5, 70)))

#------------------------------------------------------------#
'''





