'''
#------------------------------------------------------------#
Question-14:
Write a Python program to find the index of an item in a tuple.

Input:
t=10,25,'python','java',True

Output:
0 --> 10
1 --> 25
2 --> python
3 --> java
4 --> True

Hints:


Solution:
t=10,25,'python','java',True

def find_indeX(t):
    for i in range(len(t)):
        print(i,"-->",t[i])
find_indeX(t)

#------------------------------------------------------------#
'''


