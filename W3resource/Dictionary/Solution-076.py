
#------------------------------------------------------------#
Question-76:
Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.

Input:
['a', 'b', 'c', 'd', 'e', 'f']
[1, 2, 3, 4, 5]

Output:
Combine the values of the said two lists into a dictionary:
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Hints:


Solution:
key=['a', 'b', 'c', 'd', 'e', 'f']
val=[1, 2, 3, 4, 5]

#Type-1:-------------------------------------
def make_key_val(key,val):
    dic={}
    for i in range(len(val)):
        dic[key[i]]=val[i]
    print(dic)

make_key_val(key,val)

#Type-2:-------------------------------------
def make_key_val(key,val):
    res=dict(zip(key,val))
    print(res)

make_key_val(key,val)

#------------------------------------------------------------#

