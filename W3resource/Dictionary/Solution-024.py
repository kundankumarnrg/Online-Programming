
#------------------------------------------------------------#
Question-24:
Write a Python program to create a dictionary from a string.

Input:
str_val='w3resource'

Output:
{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

Hints:


Solution:
str_val='w3resource'

def track_count_letters(str_val):
    dic={}
    for ch in str_val:
        dic[ch]=dic.get(ch,0)+1
    print(dic)

#------------------------------------------------------------#


