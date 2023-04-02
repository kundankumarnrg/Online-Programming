'''
#------------------------------------------------------------#
Question-20:
Write a Python program to access the index of a list.

Input:
sample_val=[5, 15, 35, 8, 98]

Output:
0 -- 5
1 -- 15
2 -- 35
3 -- 8
4 -- 98

Hints:


Solution:
sample_val=[5, 15, 35, 8, 98]

def access_index_wise(sample_val):
    for ind in range(len(sample_val)):
        print(ind,"--",sample_val[ind])

access_index_wise(sample_val)

#------------------------------------------------------------#
'''
