
#------------------------------------------------------------#
Question-55:
Write a Python program to access dictionary key's element by index.

Input:
num = {'physics': 80, 'math': 90, 'chemistry': 86}

Output:
Expected Output:
physics
math
chemistry

Hints:


Solution:
num = {'physics': 80, 'math': 90, 'chemistry': 86}

def access_dict_index(num):

    l=len(list(num.keys()))
    for i in range(l):
        print(list(num)[i])


access_dict_index(num)

#------------------------------------------------------------#


