'''
#------------------------------------------------------------#
Question-25:
Write a Python program to select an item randomly from a list.

Input:
lst_val=[1,2,3,4,5,6,7,8,9]

Output:
9
4

Hints:
1. import random
2. random.choice()

Solution:
"""
Note:
Use random.choice() 
import random
"""

import random
lst_val=[1,2,3,4,5,6,7,8,9]

def select_random_ele_list(lst_val):
    val=random.choice(lst_val)
    print(val)

select_random_ele_list(lst_val)

#------------------------------------------------------------#
'''
