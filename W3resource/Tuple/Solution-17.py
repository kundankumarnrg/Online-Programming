'''
#------------------------------------------------------------#
Question-:
Write a Python program to unzip a list of tuples into individual lists.

Input:
t=[(1,'python'),(2,'java'),(3,'django')]

Output:
{1: 'python', 2: 'django', 3: 'flask'}

Hints:


Solution:
t=[(1,'python'),(2,'java'),(3,'django')]

def unzip(t):
    return list(zip(*t))
print(unzip(t))

#------------------------------------------------------------#
'''

