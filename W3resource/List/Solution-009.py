'''
#------------------------------------------------------------#
Question-9:
Write a Python program to clone or copy a list.

input:
lst=[1,2,3,4,5]

output:
lst2=[1,2,3,4,5]

Hints:


Solution:
lst=[1,2,3,4,5]

#Type-1:-------------------------------#

def clone(lst):
    print("lst: ",lst)
    lst2=lst[::]
    print("lst2: ",lst2)
clone(lst)


#Type-3:-----------------------------#

import copy as cp
def copy(lst):
    print("lst: ",lst)
    lst2=cp.copy(lst)
    print("lst2: ",lst2)
copy(lst)


#Type-3:-----------------------------#

import copy as cp 
def deepcopy(lst):
    print("lst: ",lst)
    lst2=cp.deepcopy(lst)
    print("lst2: ",lst2)
deepcopy(lst)


#------------------------------------------------------------#
'''





