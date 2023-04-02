'''
#------------------------------------------------------------#
Question-25:
Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

Input:
    s1={1, 2, 3, 4, 5, 6}
    s2={3, 4, 5, 6, 7, 8}

Output:
    Missing numbers in the second set as compared to the first:
    {1, 2}
    Missing numbers in the first set as compared to the second:
    {8, 7}
    Missing numbers in the second set as compared to the first:
    {1, 2}
    Missing numbers in the first set as compared to the second:
    {8, 7}

Hints:


Solution:
s1={1, 2, 3, 4, 5, 6}
s2={3, 4, 5, 6, 7, 8}

#Type-1:---------------------------------------
def missing_num_secondset_compare_first_set_and_voice_varsa(s1,s2):
    res1=set()
    res2=set()
    for val in s1:
        if val not in s2:
            res1.add(val)
    print("Missing numbers in the second set as compared to the first:")
    print(res1)

    for val in s2:
        if val not in s1:
            res2.add(val)
    print("Missing numbers in the first set as compared to the second:")
    print(res2)

missing_num_secondset_compare_first_set_and_voice_varsa(s1,s2)

#Type-2:------------------------------------------
def missing_num_secondset_compare_first_set_and_voice_varsa(s1,s2):
    res1=s1.difference(s2)
    res2=s2.difference(s1)

    print("Missing numbers in the second set as compared to the first:")
    print(res1)

    print("Missing numbers in the first set as compared to the second:")
    print(res2)

missing_num_secondset_compare_first_set_and_voice_varsa(s1,s2)

#------------------------------------------------------------#
'''
