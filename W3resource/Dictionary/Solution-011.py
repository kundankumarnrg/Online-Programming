
#------------------------------------------------------------#
Question-11:
Write a Python program to multiply all the items in a dictionary.

Input:
my_dict = {'data1':100,'data2':-54,'data3':247}

Output:
Multiplication of dict val:  -1333800


Hints:


Solution:
my_dict = {'data1':100,'data2':-54,'data3':247}

#Type-1:--------------------------------------
def multiply_dict(my_dict):
    mul=1
    for val in my_dict.values():
        mul=mul*val
    print("Multiplication of dict val: ",mul)

multiply_dict(my_dict)


#Type-2:--------------------------------------
def multiply_dict1(my_dict):
    mul=1
    for key in my_dict:
        mul=mul*my_dict[key]
    print("Multiplication of dict val: ",mul)

multiply_dict1(my_dict)

#------------------------------------------------------------#

