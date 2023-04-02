'''
#------------------------------------------------------------#
Question-:
Write a Python program to convert a given string list to a tuple.

Input:
python 3.0

Output:
('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0') 	 <class 'tuple'>

Hints:


Solution:
str1="python 3.0"

def convert_string_tuple(str1):
    print(str1,"\t",(type(str1)))
    t=tuple(str1)
    print(t,"\t",type(t))
convert_string_tuple(str1)

#------------------------------------------------------------#
'''
