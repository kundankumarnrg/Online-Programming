'''
#------------------------------------------------------------#
Question-10:
Write a Python program to check if a set is a subset of another set.

Input:
setc1=set(['ram','sita','krishana'])
subset=set(['ram','sita'])


Output:
True


Hints:


Solution:
setc1=set(['ram','sita','krishana'])
subset=set(['ram','sita'])

#Type-1:----------------------------------
def find_subset(setc1,subset):
    print(subset.issubset(setc1))
find_subset(setc1,subset)

#Type-2:---------------------------------
def find_subset1(setc1,subset):
    f=0

    for val in subset:
        if val in setc1:
           f=f+1
        else:
            f=0
    print("True" if (f==len(subset)) else "False")
find_subset1(setc1,subset)

#------------------------------------------------------------#
'''


