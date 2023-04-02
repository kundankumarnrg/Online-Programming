'''
#------------------------------------------------------------#
Question-9:
Write a Python program to create a symmetric difference.

Input:
    setc1 = set(["green", "blue"])
    setc2 = set(["blue", "yellow"])
    setn3 = set([1, 1, 2, 3, 4, 5])
    setn4 = set([1, 5, 6, 7, 8, 9])

Output:
    {'green', 'blue'}
    {'blue', 'yellow'}
    find semetric difference: 
    {'green', 'yellow'}
    
    find semetric difference: 
    {2, 3, 4, 6, 7, 8, 9}

Hints:


Solution:
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
setn3 = set([1, 1, 2, 3, 4, 5])
setn4 = set([1, 5, 6, 7, 8, 9])

def find_symetric_difference(setc1,setc2,setn3,setn4):
    print(setc1)
    print(setc2)
    print("find semetric difference: ")
    print(setc1.symmetric_difference(setc2))
    
    print("find semetric difference: ")
    print(setn3.symmetric_difference(setn4))

find_symetric_difference(setc1,setc2,setn3,setn4)

#------------------------------------------------------------#
'''


