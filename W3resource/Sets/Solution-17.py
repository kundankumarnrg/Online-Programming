'''
#------------------------------------------------------------#
Question-17:
Write a Python program to check if two given sets have no elements in common.

Input:
    s1=set([1,2,3,])
    s2=set([4,5,6])
    s3=set([7,8,9,6])

Output:
    common element in either s2 and s2


Hints:


Solution:
s1=set([1,2,3,])
s2=set([4,5,6])
s3=set([7,8,9,6])

def check_no_common_ele(s1,s2,s3):
    c=0
    for val in s1:
        if val in s2 or s3:
            c=1
    print("No commom element s1, s2 or s3" if c==0 else "common element in either s2 and s2")
check_no_common_ele(s1,s2,s3)

#------------------------------------------------------------#
'''

