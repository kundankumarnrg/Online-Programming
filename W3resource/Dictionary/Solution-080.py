
#------------------------------------------------------------#
Question-80:
Write a Python program to find the key of the maximum value in a dictionary. 

Input:
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

Output:
Finds the key of the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')

Hints:


Solution:
dict_val={'Theodore': 19, 'Roxanne': 21, 'Mathew': 21, 'Betty': 20}

def find_max_min_val_val(dict_val):
    res=[]
    lst=list(dict_val.values())
    for key,val in dict_val.items():
        if val==min(lst) or val==max(lst):
            res.append(key)
    print(res)


find_max_min_val_val(dict_val)

#------------------------------------------------------------#


