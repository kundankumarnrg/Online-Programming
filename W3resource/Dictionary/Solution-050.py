
#------------------------------------------------------------#
Question-50:
A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.

Input:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

Output:
Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []}

Hints:


Solution:
simple_data={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

#Type-1:---------------------------------
def remove_list_val(simple_data):
    print(simple_data)
    res={key:[] for key,val in simple_data.items()}
    print(res)
remove_list_val(simple_data)

#Type-2:---------------------------------
def remove_list_val1(simple_data):
    print("\n",simple_data)
    for key,val in simple_data.items():
        simple_data[key].clear()
    print(simple_data)
remove_list_val1(simple_data)


#------------------------------------------------------------#








