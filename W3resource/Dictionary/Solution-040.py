
#------------------------------------------------------------#
Question-40:
Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.

Input:
{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

Output:
15
25
35
x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

Hints:


Solution:
dic={"X":(list(range(11,20))),"Y":(list(range(21,30))),"Z":(list(range(31,40)))}
def display_val(dic):
    print(dic['X'][4])
    print(dic['Y'][4])
    print(dic['Z'][4])

    for k,v in dic.items():
        print(k,'has value',v)

display_val(dic)

#------------------------------------------------------------#


