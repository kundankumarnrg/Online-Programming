'''
#------------------------------------------------------------#
Question-22:
Write a Python program to find the index of an item in a specified list.

Input:
lst=[10,20,30,40,50]

Output:
10 -- 0
20 -- 1
30 -- 2
40 -- 3
50 -- 4

Hints:


Solution:
lst=[10,20,30,40,50]

def find_index_list_element(lst):
    for val in lst:
        print(val,"--",lst.index(val))
find_index_list_element(lst)

#------------------------------------------------------------#
'''
