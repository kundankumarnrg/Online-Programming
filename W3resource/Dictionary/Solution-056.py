
#------------------------------------------------------------#
Question-56:
Write a Python program to convert a dictionary into a list of lists.

Input:
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

Output:
Convert the said dictionary into a list of lists:
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

Convert the said dictionary into a list of lists:
[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

Hints:


Solution:
dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dic2={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

#Type-1:----------------------------------
def convert_dict_into_list(dic):
    lst=[]
    for key,val in dic.items():
        lst.append([key,val])
    print(lst)
convert_dict_into_list(dic)
convert_dict_into_list(dic2)

#Type-2:----------------------------------
def convert_dict_into_list1(dic):
    res=[[k,v] for k,v in dic.items()]
    print(res)
convert_dict_into_list1(dic)
convert_dict_into_list(dic2)


#------------------------------------------------------------#


