
#------------------------------------------------------------#
Question-70:
Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.

Input:
lst=[1,2,3,4]

Output:
{1: 1, 2: 4, 3: 9, 4: 16}

Hints:


Solution:
lst=[1,2,3,4]

def map_val_dict(lst):
    res={i:i*i for i in lst}
    print(res)
map_val_dict(lst)

#------------------------------------------------------------#




