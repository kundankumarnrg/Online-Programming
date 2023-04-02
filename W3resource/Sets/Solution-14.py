'''
#------------------------------------------------------------#
Question-14:
Write a Python program to find the maximum and minimum values in a set.

Input:
    s=set([1,4,5,2,3,6,9,8,7])
    s1=set([1,4,5,2,3,6,9,8,7])

Output:
    Min value: 1
    Max value: 9

Hints:


Solution:
s=set([1,4,5,2,3,6,9,8,7])
s1=set([1,4,5,2,3,6,9,8,7])
#Type-1:-------------------------------
def find_min_max_val(s):
    minv=min(s)
    maxv=max(s)
    print("Min value: ",minv)
    print("Max value:",maxv)

find_min_max_val(s)

#Type-2:----------------------------
def find_max_min_val(s):
    s=sorted(s)
    print("Min value: ",s[0])
    print("max value: ",s[len(s)-1])
find_max_min_val(s)

#------------------------------------------------------------#
'''



