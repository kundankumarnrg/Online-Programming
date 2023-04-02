'''
#------------------------------------------------------------#
Question-8:
Write a Python program to create the colon of a tuple.

Input:
t = ("HELLO", 5, [], True)

Output:
t = ("HELLO", 5, [], True) 

Hints:
-slicing
-copy
-deepcopy


Solution:
t = ("HELLO", 5, [], True) 

#Type-1:-----------------------------
def create_colon(t):
    print(t)
    cl=t[:]
    print(type(cl))
    print(cl)
create_colon(t)

#Type-2:---------------------------
import copy as cp 
def create_colon1(t):
    print(t)
    cl1=cp.copy(t)
    print(type(cl1))
    print(cl1)

create_colon1(t)

#Type-3:---------------------------
import copy as cp 
def create_colon1(t):
    print(t)
    cl2=cp.deepcopy(t)
    print(type(cl2))
    print(cl2)

create_colon1(t)


#------------------------------------------------------------#
'''
