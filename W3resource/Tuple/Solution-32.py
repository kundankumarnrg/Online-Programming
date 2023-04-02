'''
#------------------------------------------------------------#
Question-32:
Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.

Input:
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

Output:
[3, 5, 7]
[9, -1, 7, 8]

Hints:


Solution:
t=[(1, 2), (2, 3), (3, 4)]

def compute_sum_all_elements(t):
    sum=0
    lst=[]
    for val in t:
        sum=0
        for v in val:
            sum=sum+v
        lst.append(sum)
    return lst
print(compute_sum_all_elements(t=[(1, 2), (2, 3), (3, 4)]))
print(compute_sum_all_elements(t=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]))

#------------------------------------------------------------#
'''
