'''
#------------------------------------------------------------#
Question-8:
Write a Python program to check if a list is empty or not.

input:
lst=[]
lst=[1,2]

output:
True
False


Hints:


Solution:
lst=[]

#Type-1:------------------------------------#

def check_list_empty(lst):
    l=len(lst)
    print("empty" if l==0 else "Not empty")
check_list_empty(lst)


#Type-2:------------------------------------#

def empty_or_not(lst):
    print("empty" if not lst else "Not empty")
empty_or_not(lst)


#------------------------------------------------------------#
'''
