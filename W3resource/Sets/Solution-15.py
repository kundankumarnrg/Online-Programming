'''
#------------------------------------------------------------#
Question-15:
Write a Python program to find the length of a set.

Input:
    s=([1, 2, 3, 4, 5, 6])

Output:
    6

Hints:


Solution:
s=([1, 2, 3, 4, 5, 6])

#Type-1:---------------------
def find_length(s):
    return len(s)
print(find_length(s))

#Type-2:--------------------
def find_len(s):
    c=0
    for i in s:
        c=c+1
    print(c)

find_len(s)

#------------------------------------------------------------#
'''

