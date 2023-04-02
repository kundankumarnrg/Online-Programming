'''
#------------------------------------------------------------#
Question-58:
Write a Python program to replace the last element in a list with another list.

Input:
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

Output:
res=[1, 3, 5, 7, 9, 2, 4, 6, 8] 

Hints:


Solution:
lst=[1, 3, 5, 7, 9, 10]
rep=[2, 4, 6, 8]
#rep_poss=lst

def replace_list(lst,rep):
    res=[]
    print(lst)
    res=lst[0:((len(lst))-1)]+rep
    print(res)
    
replace_list(lst,rep)



#------------------------------------------------------------#
'''

