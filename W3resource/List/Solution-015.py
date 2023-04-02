'''
#------------------------------------------------------------#
Question-15:
Write a Python program to shuffle and print a specified list.

Input:
lst=[1,2,3,4,5]

Output:
[3, 1, 2, 5, 4]
[2, 3, 5, 4, 1]
[4, 3, 1, 5, 2]
[1, 3, 5, 2, 4]
[1, 5, 2, 4, 3]
[5, 1, 2, 4, 3]
[2, 4, 1, 3, 5]
[3, 2, 4, 5, 1]
[3, 1, 5, 4, 2]
[4, 1, 3, 5, 2]

Hints:
1. import random 
2. random.shuffle()

Solution:
lst=[1,2,3,4,5]

import random
def suffle_list(lst):
    for i in range(10):
        random.shuffle(lst)
        print(lst)
suffle_list(lst)

#------------------------------------------------------------#
'''
