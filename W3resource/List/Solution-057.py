'''
#------------------------------------------------------------#
Question-57:
Write a Python program to check if all items in a given list of strings are equal to a given string.

Input:
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

Output:
False
False

Hints:


Solution:
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

def all_string_same(color1,color2):
    val1=color1[0]
    val2=color2[0]
    c=0
    for value in color1:
        if val1==value:
            c=c+1
    print("True" if c==len(color1) else "False")

    c1=0
    for value in color2:
        if val1==value:
            c1=c1+1
    print("True" if c1==len(color2) else "False")
all_string_same(color1,color2)

#------------------------------------------------------------#
'''

