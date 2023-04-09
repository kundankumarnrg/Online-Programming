
#------------------------------------------------------------#
Question-78:
Write a Python program to create a flat list of all the keys in a flat dictionary.

Input:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

Output:
Create a flat list of all the keys of the said flat dictionary:
['Theodore', 'Roxanne', 'Mathew', 'Betty']

Hints:


Solution:
dict_val={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

#Type-1:---------------------------------
res=list(dict_val.keys())
print(res)

#Type-2:---------------------------------
lst=[]
for k in dict_val.keys():
    lst.append(k)
print(lst)

#------------------------------------------------------------#

