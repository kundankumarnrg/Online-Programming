
#------------------------------------------------------------#
Question-28:
Write a Python program to sort a list alphabetically in a dictionary.

Input:
num = {'n14': [2, 3, 1], 'n2': [5, 1, 2], 'n43': [3, 2, 4]}

Output:
{'n14': [1, 2, 3], 'n2': [1, 2, 5], 'n43': [2, 3, 4]}
{'num1': [1, 5], 'num2': [2, 4], 'num3': [4, 7]}

Hints:


Solution:
def sorted_dict_val(num):
    res={x:sorted(y) for x,y in num.items()}
    print(res)

sorted_dict_val(num = {'n14': [2, 3, 1], 'n2': [5, 1, 2], 'n43': [3, 2, 4]})
sorted_dict_val(num={"num1":(5,1),"num2":(4,2),"num3":(7,4)})

#------------------------------------------------------------#






