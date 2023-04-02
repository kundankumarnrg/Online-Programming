'''
#------------------------------------------------------------#
Question-11:
Write a Python program to create a shallow copy,deep copy, of sets.

Input:
    s = set(["Red", "Green"])

Output:
    res={'Red', 'Green'}

Hints:
    Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object

Solution:
s = set(["Red", "Green"])

#Type-1:------------------------
import copy as cp
def copy_set(s):
    print(s)
    res=cp.copy(s)
    print(res)
copy_set(s)

#Type-2:-----------------------
import copy as cp
def copy_set_ele(s):
    print(s)
    res=cp.deepcopy(s)
    print(res)
copy_set(s)

#Type-3:----------------------
import copy as cp
def copy_set_ele(s):
    print(s)
    res=s[:]
    print(res)
copy_set(s)

#------------------------------------------------------------#
'''


