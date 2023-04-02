'''
#------------------------------------------------------------#
Question-45:
Write a Python program to convert a pair of values into a sorted unique array.

Input:
lst=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Hints:


Solution:
lst=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]

#Type-1:---------------------------------------------#
def sorted_pair_unique_val(lst):
    res=[]
    for values in lst:
        for val in values:
            if val not in res:
                res.append(val)
    print(sorted(res))

sorted_pair_unique_val(lst)


#Type-2:--------------------------------------------#
def sorted_pair_unique_values(lst):
    res2=[val for values in lst  for val in values]
    print(list(sorted(set(res2))))

sorted_pair_unique_values(lst)

#------------------------------------------------------------#
'''

