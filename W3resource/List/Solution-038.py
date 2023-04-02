'''
#------------------------------------------------------------#
Question-38:
Write a Python program to change the position of every n-th value to the (n+1)th in a list.

Input:
Sample list: [0,1,2,3,4,5]

Output:
res= [1, 0, 3, 2, 5, 4]

Hints:


Solution:
lst=[1,2,3,4,5,6]

def change_possiotion_list_element(lst):
    print(lst)
    for i in range(0,len(lst),2):
        lst[i],lst[i+1]=lst[i+1],lst[i]
    print(lst)
change_possiotion_list_element(lst)

#------------------------------------------------------------#
'''
