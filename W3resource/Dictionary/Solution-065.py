
#------------------------------------------------------------#
Question-65:
Write a Python program to get the total length of all values in a given dictionary with string values.

Input:
{'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

Output:
20

Hints:


Solution:
dict_val={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

def count_length_values(dict_val):
    c=0
    for val in dict_val.values():
        c=c+len(val)
    print(c)
count_length_values(dict_val)

#------------------------------------------------------------#



