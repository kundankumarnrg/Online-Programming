'''
#------------------------------------------------------------#
Question-29:
Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.

Input:
    num=[1,2,5,8,7,4,1,5,6,3,9,8,5,2,1,4]

Output:
    Third largest number of the said list of numbers: 7

Hints:


Solution:
num=[1,2,5,8,7,4,1,5,6,3,9,8,5,2,1,4]

def find_third_larges_ele(num):
    print(num)
    res=list(sorted(set(num)))
    print("Third largest number of the said list of numbers:",res[-3])
find_third_larges_ele(num)

#------------------------------------------------------------#
'''

