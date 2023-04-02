'''
#------------------------------------------------------------#
Question-20:
Write a Python program to remove the intersection of a second set with a first set.

Input:
    sn1 = {1,2,3,4,5}
    sn2 = {4,5,6,7,8}

Output:
    Remove the intersection of a 2nd set from the 1st set using difference_update():
    {6, 7, 8}
    {1, 2, 3, 4, 5}

Hints:


Solution:
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}

def remove_intersection_second_first_set(sn1,sn2):
    print(sn1)
    print(sn2)
    for val in sn2:
        if val in sn1:
            sn1.remove(val)
    print("Remove the intersection of a 2nd set from the 1st set using difference_update():")       
    print(sn1)
    print(sn2)
remove_intersection_second_first_set(sn2,sn1)

#------------------------------------------------------------#
'''
