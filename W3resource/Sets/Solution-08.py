'''
#------------------------------------------------------------#
Question-8:
Write a Python program to create set difference.

Input:
    setc1 = set(["green", "blue"])
    setc2 = set(["blue", "yellow"])

Output:
    difference between set1 and set2
    {'green'}

    Difference between set2 and set1
    {'yellow'}
    difference between set1 and set2
    {'green'}

    Difference between set2 and set1
    {'yellow'}

Hints:


Solution:
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])

#Type-1:------------------------------------------
def set_difference(setc1,setc2):
    print("difference between set1 and set2")
    print(setc1.difference(setc2))

    print("\n Difference between set2 and set1")
    print(setc2.difference(setc1))
    
set_difference(setc1,setc2)

#Type-2:-----------------------------------------
def set_difference1(setc1,setc2):
    print("difference between set1 and set2")
    print(setc1-setc2)

    print("\n Difference between set2 and set1")
    print(setc2-setc1)
    
set_difference1(setc1,setc2)

#------------------------------------------------------------#
'''


