'''
#------------------------------------------------------------#
Question-9:
Write a Python program to find repeated items in a tuple.

Input:
t=10,20,55,4,7,8,9,5,2,1,4,5,6,3,2

Output:
{10: 1, 20: 1, 55: 1, 4: 2, 7: 1, 8: 1, 9: 1, 5: 2, 2: 2, 1: 1, 6: 1, 3: 1}

1 : 1, 2 : 2, 3 : 1, 4 : 2, 5 : 2, 6 : 1, 7 : 1, 8 : 1, 9 : 1, 10 : 1, 20 : 1, 55 : 1, 

Hints:


Solution:
t=10,20,55,4,7,8,9,5,2,1,4,5,6,3,2

#Type-1:--------------------------------
def find_reapeted_ele(t):
    dic={}
    for val in t:
        dic[val]=dic.get(val,0)+1
    print(dic)
find_reapeted_ele(t)

#Type-2:--------------------------------
def find_reapeted_ele1(t):
    for val in sorted(set(t)):
        c=0
        c=t.count(val)
        print(val,":",c,end=", ")
    
find_reapeted_ele1(t)

#------------------------------------------------------------#
'''
