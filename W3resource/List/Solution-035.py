'''
#------------------------------------------------------------#
Question-35:
Write a Python program to create a list by concatenating a given list with a range from 1 to n.

Input:
Sample list : ['p', 'q']
n =5

Output:
['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

Hints:


Solution:
lst=['p','q']
n=5
def formate_output(lst,n):
    new_lst=[]
    for i in range(1,n+1):
        for val in lst:
            tem=""
            tem=val+str(i)
            new_lst.append(tem)
    print(new_lst)
formate_output(lst,n)

#------------------------------------------------------------#
'''
