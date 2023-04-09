
#------------------------------------------------------------#
Question-49:
Write a Python program to convert string values of a given dictionary into integer/float datatypes. 

Input:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

Output:
String values of a given dictionary, into integer types:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

String values of a given dictionary, into float types:
[{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
Hints:


Solution:
def convert_string_val_dict_int(lst):
    lst1=[]
    dic={}
    for value in lst:
        dic={}
        for key,val in value.items():
            dic[key]=int(val)
        lst1.append(dic)
    print(lst1)


convert_string_val_dict_int([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}])


def convert_string_val_dict_float(lst):
    lst1=[]
    dic={}
    for value in lst:
        dic={}
        for key,val in value.items():
            dic[key]=float(val)
        lst1.append(dic)
    print(lst1)
convert_string_val_dict_float([{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}])


#------------------------------------------------------------#

#[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

