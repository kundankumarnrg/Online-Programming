
#------------------------------------------------------------#
Question-53:
Write a Python program to find the length of a dictionary of values.

Input:
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

Output:
Length of dictionary values:
{'red': 3, 'green': 5, 'black': 5, 'white': 5}

Length of dictionary values:
{'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

Hints:


Solution:
dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dic_val={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

#Type-1:------------------------------
def find_dic_val_lenght(dic):
    dic1={}
    for val in dic.values():
        l=len(val)
        dic1[val]=l
    print(dic1)
find_dic_val_lenght(dic)
find_dic_val_lenght(dic_val)


#Type-2:------------------------------
def find_dic_val_length(dic):
    res={key:len(val) for key, val in dic.items()}
    print(res)
find_dic_val_lenght(dic)
find_dic_val_lenght(dic_val)

#------------------------------------------------------------#




