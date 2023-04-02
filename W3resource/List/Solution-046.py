'''
#------------------------------------------------------------#
Question-46:
Write a Python program to select the odd items from a list.

Input:
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Output:
[1, 3, 5, 7, 9] 

Hints:


Solution:
my_list=[1,2,3,4,5,6,7,8,9,0,12,23,44,50]


#Type-1:------------------------------------
def odd_number(my_list):
    print(my_list)
    lst=[]
    for val in my_list:
        if val%2!=0:
            lst.append(val)
    print("Odd List:",lst)

odd_number(my_list)


#Type-2:------------------------------------
def odd_number_list(my_list):
    print(my_list)
    lst=[val for val in my_list if val%2!=0]
    print("Odd List:",lst)
odd_number_list(my_list)

#------------------------------------------------------------#
'''

