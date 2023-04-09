
#------------------------------------------------------------#
Question-34:
Write a Python program to count the number of items in a dictionary value that is a list.

Input:
dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

Output:
5

Hints:


Solution:
dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

def count_num_items_dict_val_list(dic):
    c=0
    for val in dic.values():
        c=c+len(val)
    print(c)

count_num_items_dict_val_list(dic)

#------------------------------------------------------------#

