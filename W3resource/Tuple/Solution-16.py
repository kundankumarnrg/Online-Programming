'''
#------------------------------------------------------------#
Question-:
Write a Python program to convert a tuple to a dictionary.

Input:
t=((1,'python'),(2,"django"),(3,"flask"))

Output:
{1: 'python', 2: 'django', 3: 'flask'}


Hints:


Solution:
t=((1,'python'),(2,"django"),(3,"flask"))

#Tpe-1:-------------------------------
def convert_tuple_dict(t):
    dic={}
    for val in t:
        k,v=val
        dic[k]=v
    print(dic)
convert_tuple_dict(t)

#------------------------------------------------------------#
'''


