'''
#------------------------------------------------------------#
Question-30:
Write a Python program to get the frequency of elements in a list.
Input:
lst=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

Output:
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
40 : 2, 10 : 4, 50 : 2, 20 : 4, 30 : 1, 

Hints:


Solution:
lst=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

#Type-1:----------------------#
def frequent_element1(lst):
    dic={}
    for i in lst:
        dic[i]=dic.get(i,0)+1
    print(dic)

frequent_element1(lst)

#Type-2:--------------------#
def frequent_element(lst):
    for val in set(lst):
        c=0
        c=lst.count(val)
        print(val,":",c,end=", ")

frequent_element(lst)

#------------------------------------------------------------#
'''





