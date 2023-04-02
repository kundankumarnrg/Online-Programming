'''
#------------------------------------------------------------#
Question-7:
Write a Python program to create a union of sets.

Input:
    s1=set([1,2,3,4,5,6])
    s2=set([4,5,6,7,8,9])

Output:
    {1, 2, 3, 4, 5, 6}
    {4, 5, 6, 7, 8, 9}
    union between s1 and s2:
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    {1, 2, 3, 4, 5, 6}
    {4, 5, 6, 7, 8, 9}
    union between s1 and s2: 
    {1, 2, 3, 4, 5, 6, 7, 8, 9}

Hints:


Solution:
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#Type-1:---------------------------------------
def find_union(s1,s2):
    print(s1)
    print(s2)
    print("union between s1 and s2:")
    return s1.union(s2)
print(find_union(s1,s2))

#Type-2:--------------------------------------
def find_union(s1,s2):
    print(s1)
    print(s2)
    print("union between s1 and s2: ")
    res=s1 | s2
    print(res)
    
find_union(s1,s2)

#------------------------------------------------------------#
'''

