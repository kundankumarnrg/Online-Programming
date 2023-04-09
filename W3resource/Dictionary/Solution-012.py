
#------------------------------------------------------------#
Question-12:
Write a Python program to remove a key from a dictionary.

Input:
dic={'a':1,'b':2,'c':3,'d':4}

Output:
{'a': 1, 'b': 2, 'c': 3}

Hints:


Solution:
dic={'a':1,'b':2,'c':3,'d':4}

def remove_dict_key(dic,key):
    print(dic)
    del dic[key]
    print(dic)
    
remove_dict_key(dic,key='d')

#------------------------------------------------------------#

