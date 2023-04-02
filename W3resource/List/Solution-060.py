'''
#------------------------------------------------------------#
Question-60:
Write a Python program to find a tuple, the smallest second index value from a list of tuples.

Input:
value=[(4, 11), (1, 12), (6, 10),(12,14),(15,1)]

Output:
(15, 1)

Hints:


Solution:
value=[(4, 11), (1, 12), (6, 10),(12,14),(15,1)]

def find_second_ind_smallest_Number(value):
    tem=value[0][1]
    for val in value:
        if val[1]<=tem:
            tem=val[1]
            res=val
    print(res)
find_second_ind_smallest_Number(value)

#------------------------------------------------------------#
'''




