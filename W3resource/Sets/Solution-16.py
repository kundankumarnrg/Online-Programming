'''
#------------------------------------------------------------#
Question-16:
Write a Python program to check if a given value is present in a set or not.

Input:
    s=set(['ram',True,10.23,'sita','ramkrishana',10,20])

Output:
    Not present
    present

Hints:


Solution:
s=set(['ram',True,10.23,'sita','ramkrishana',10,20])

def find_val_present_or_not(s,val):
    print("present" if val in s else "Not present")

find_val_present_or_not(s,12)
find_val_present_or_not(s,'sita')

#------------------------------------------------------------#
'''



