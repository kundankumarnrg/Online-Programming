'''
#------------------------------------------------------------#
Question-31:
Write a Python program to compute the element-wise sum of given tuples.

Input:
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)

Output:
Element-wise sum of the said tuples:
(6, 9, 8, 6)

Hints:


Solution:
t1=(1, 2, 3, 4)
t2=(3, 5, 2, 1)
t3=(2, 2, 3, 1)

def Element_wise_sum(t1,t2,t3):
    lst=[]
    sum=0
    for i in range(len(t1)):
        sum=0
        sum=t1[i]+t2[i]+t3[i]
        lst.append(sum)
    print(t1)
    print(t2)
    print(t2)
    print("summ of element wise:")
    print(tuple(lst))

Element_wise_sum(t1,t2,t3)

#------------------------------------------------------------#
'''



