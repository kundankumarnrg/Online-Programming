
#------------------------------------------------------------#
Question-79:
Write a Python program to create a flat list of all the values in a flat dictionary.

Input:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

Output:
Create a flat list of all the values of the said flat dictionary:
[19, 20, 21, 20]

Hints:


Solution:
dict_val={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

#Type-1:-------------------------------
res=list(dict_val.values())
print(res)

#Type-2:-------------------------------
lst=[]
for v in dict_val.values():
    lst.append(v)
print(lst)

#------------------------------------------------------------#


