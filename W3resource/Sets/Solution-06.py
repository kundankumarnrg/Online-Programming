'''
#------------------------------------------------------------#
Question-6:
Write a Python program to create an intersection of sets.

Input:
    s1=set([1,2,3,4,5,6])
    s2=set([4,5,6,7,8,9])

Output:
    {1, 2, 3, 4, 5, 6}
    {4, 5, 6, 7, 8, 9}
    intersection between s1 and s2:
    {4, 5, 6}
    {1, 2, 3, 4, 5, 6}
    {4, 5, 6, 7, 8, 9}
    Intersetion between s1 and s2: 
    {4, 5, 6}

Hints:


Solution:
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#Type-1:---------------------------------------
def find_intersection(s1,s2):
    print(s1)
    print(s2)
    print("intersection between s1 and s2:")
    return s1.intersection(s2)
print(find_intersection(s1,s2))

#Type-2:--------------------------------------
def find_intersetions(s1,s2):
    print(s1)
    print(s2)
    print("Intersetion between s1 and s2: ")
    res=s1 & s2
    print(res)
    
find_intersetions(s1,s2)


#------------------------------------------------------------#
'''








