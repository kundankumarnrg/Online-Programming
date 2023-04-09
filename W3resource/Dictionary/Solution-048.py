
#------------------------------------------------------------#
Question-48:
 Write a Python program to remove a specified dictionary from a given list.

Input:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:

Output:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

Hints:


Solution:
simple_data=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
#removeing data
rv="#FF0000"

def remove_ele(simple_data,rv):
    print(simple_data)
    for val in simple_data:
        if val['id']==rv:
            simple_data.remove(val)

    print(simple_data)
remove_ele(simple_data,rv)

#------------------------------------------------------------#


