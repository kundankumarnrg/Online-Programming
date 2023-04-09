
#------------------------------------------------------------#
Question-9:
Write a Python program to iterate over dictionaries using for loops.

Input:
d = {'Red': 1, 'Green': 2, 'Blue': 3} 

Output:
Red : 1, Green : 2, Blue : 3,

Hints:


Solution:
d = {'Red': 1, 'Green': 2, 'Blue': 3} 

def iterator_dic_using_forloop(d):
    for key,val in d.items():
        print(key,":",val,end=", ")
iterator_dic_using_forloop(d)

#------------------------------------------------------------#


