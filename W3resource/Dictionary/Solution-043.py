
#------------------------------------------------------------#
Question-43:
Write a Python program to convert more than one list to a nested dictionary.

Input:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]

Output:
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

Hints:


Solution:
lst_val1=['S001', 'S002', 'S003', 'S004']
lst_val2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
lst_val3=[85, 98, 89, 92]

def more_then_one_nested_dict(lst_val1,lst_val2,lst_val3):
    dic1,dic2={},{}
    lst=[]
    for i in range(len(lst_val1)):
        dic2={}
        dic2[(lst_val2[i])]=lst_val3[i]
        dic1[(lst_val1[i])]=dic2
        lst.append(dic1)
        dic1={}
    print(lst)
more_then_one_nested_dict(lst_val1,lst_val2,lst_val3)

#------------------------------------------------------------#


