
#------------------------------------------------------------#
Question-64:
Write a Python program that creates key-value list pairings within a dictionary.

Input:
{1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

Output:
A key-value list pairings of the said dictionary:
[{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

Hints:


Solution:
dict_data={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

def create_key_val_parings(dict_data):
    dic={}
    for k,v in dict_data.items():
       dic[k]=v[0]
    print([dic])

create_key_val_parings(dict_data)

#------------------------------------------------------------#



