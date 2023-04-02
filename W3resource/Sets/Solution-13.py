'''
#------------------------------------------------------------#
Question-13:
Write a Python program that uses frozensets.

Input:
    s=set([1,2,3,4,5,6])

Output:
    {1, 2, 3, 4, 5, 6} 	 <class 'set'>
    frozenset({1, 2, 3, 4, 5, 6}) 	 <class 'frozenset'>

Hints:
    Frozensets behave just like sets except they are immutable.
    x = frozenset([1, 2, 3, 4, 5])

Solution:
s=set([1,2,3,4,5,6])

def frozensets(s):
    print(s,"\t",type(s))
    fz=frozenset(s)
    print(fz,"\t",type(fz))
frozensets(s)

#------------------------------------------------------------#
'''


