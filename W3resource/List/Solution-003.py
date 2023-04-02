'''
#------------------------------------------------------------#
Question-3:
Write a Python program to get the largest number from a list.

input:
lst=[700,110,2,5,4,8,9,600,3,25,69,48,2000]

output:
res=2000

Hints:


Solution:
lst=[700,110,2,5,4,8,9,600,3,25,69,48,2000]

#Type-1:-----------------------------------#

def find_max_ele(lst):
    print("Max values: ",max(lst))
find_max_ele(lst)

#Type-2:-----------------------------------#

def find_max_val(lst):
    lst1=sorted(lst)
    print("Max val: ",lst1[-1])
find_max_val(lst)


#Type-3:-----------------------------------#

def find_max_values(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]<lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    print("Max values: ",lst[-1])
find_max_values(lst)


#Type-4:-----------------------------------#
def find_max_val(lst):
    tem=lst[0]
    for val in lst:
        if tem<val:
            tem=val
    print(tem)
find_max_val("Max values: ",lst)


#------------------------------------------------------------#
'''



#kumar kunal