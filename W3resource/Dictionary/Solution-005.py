
#------------------------------------------------------------#
Question-5:
Write a Python program to iterate over dictionaries using for loops.

Input:
dic = {'x': 10, 'y': 20, 'z': 30}

Output:
x : 10, y : 20, z : 30,

Hints:


Solution:
dic = {'x': 10, 'y': 20, 'z': 30} 

def iterate_dic(dic):
    for key,val in dic.items():
        print(key,":",val,end=", ")
iterate_dic(dic)


#------------------------------------------------------------#



