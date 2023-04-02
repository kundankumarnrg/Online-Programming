'''
#------------------------------------------------------------#
Question-5:
 Write a Python program to remove an item from a set if it is present in the set. 

Input:
    s=set([1,2,5,14,9,6,3,4])

Output:
    {1, 2, 3, 4, 5, 6, 9, 14}
    {2, 3, 4, 5, 6, 9, 14}
    {3, 4, 5, 6, 9, 14}
    {3, 5, 6, 9, 14}

Hints:


Solution:
    s=set([1,2,5,14,9,6,3,4])

    def remove_val(s):
        print(s)
        s.remove(1)
        print(s)
        s.pop()
        print(s)
        s.discard(4)
        print(s)
    remove_val(s)

#------------------------------------------------------------#
'''

