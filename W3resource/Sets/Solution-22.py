'''
#------------------------------------------------------------#
Question-22:
Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

Input:
lst=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
trg=35

Output:
[{20, 15}, {16, 19}, {17, 18}, {17, 18}, {16, 19}, {20, 15}]

Hints:


Solution:
lst=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
trg=35

def pairs_ele_sum_given_value(lst):
    res=[]
    for i in range(len(lst)):
        s=set()
        for j in range(len(lst)):
            if(lst[i]+lst[j]==trg):
                s=set([lst[i],lst[j]])
                res.append(s)
    print(res)

pairs_ele_sum_given_value(lst)

#------------------------------------------------------------#
'''

