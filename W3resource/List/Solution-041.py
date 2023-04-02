'''
#------------------------------------------------------------#
Question-41:
Write a Python program to create multiple lists.

Input:


Output:
{'1': [], '8': [], '14': [], '5': [], '17': [], '9': [], '2': [], '7': [], '16': [], '19': [], '4': [], '18': 
[], '13': [], '3': [], '15': [], '11': [], '20': [], '6': [], '12': [], '10': []}

Hints:


Solution:
def create_mutiple_list():
    dic={}
    lst=[]
    for i in range(1,10):
        dic[str(i)]=lst
    print(dic)

create_mutiple_list()

#------------------------------------------------------------#
'''



