'''
#------------------------------------------------------------#
Question-:
Write a Python program to convert a list to a tuple.

Input:
[1, 2, 3, 4, 5] 	 <class 'list'>

Output:
(1, 2, 3, 4, 5) 	 <class 'tuple'>

Hints:


Solution:
lst=[1,2,3,4,5]
def convert_list_tuple(lst):
    print(lst,"\t",(type(lst)))
    t=tuple(lst)
    print(t,"\t",(type(t)))
convert_list_tuple(lst)


#------------------------------------------------------------#
'''

