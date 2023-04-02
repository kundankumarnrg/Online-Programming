'''
#------------------------------------------------------------#
Question-19:
Write a Python program to find elements in a given set that are not in another set.

Input:
    s1=set([1,2,3,4,5,6])
    s2=set([4,5,6,7,8,9])

Output:
    {1, 2, 3}
    {1, 2, 3, 4, 5, 6}
    {4, 5, 6, 7, 8, 9}
    {1, 2, 3}

Hints:


Solution:
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#Type-1:-----------------------------------------
def find_ele_not_in_otherset(s1,s2):
    lst=[]
    for val in s1:
        if val not in s2:
            lst.append(val)
    print(set(lst))
find_ele_not_in_otherset(s1,s2)


#Type-2:-----------------------------------------
def find_ele_not_in_otherset_val(s1,s2):
    print(s1)
    print(s2)
    res=s1.difference(s2)
    print(res)
find_ele_not_in_otherset_val(s1,s2)


#------------------------------------------------------------#
'''
