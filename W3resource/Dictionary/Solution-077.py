
#------------------------------------------------------------#
Question-77:
Write a Python program to transform a dictionary into a list of tuples.

Input:
{'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

Output:
Convert the said dictionary to a list of tuples:
[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

Hints:


Solution:
dict_data={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

#Type-1:-------------------------------------
def convert_dict_into_lisoftuple(dict_data):
    lst=[]
    for key,val in dict_data.items():
        lst.append((key,val))
    print(lst)

convert_dict_into_lisoftuple(dict_data)

#Type-2:-------------------------------------
def convert_dict_into_lisoftuple(dict_data):
    res=[(key,val)for key,val in dict_data.items()]
    print(res)

convert_dict_into_lisoftuple(dict_data)

#------------------------------------------------------------#




