'''
#------------------------------------------------------------#
Question-18:
Write a Python program to generate all permutations of a list in Python.

Input:
number of term=10
num=10

Output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Solution:
term=10
num=term
#Type-1:--------------------------------------
def genrate_parmutation_list(num):
    f,s=0,1
    lst=[]
    for i in range(num):
        lst.append(f)
        f,s=s,f+s
    print(lst)
genrate_parmutation_list(num)

#Type-2:--------------------------------------
def genrate_parmutation(num):
    i=0
    f,s=0,1
    lst=[]
    while(i<num):
        lst.append(f)
        f,s=s,f+s
        i=i+1
    print(lst)

genrate_parmutation(num)

#------------------------------------------------------------#
'''
