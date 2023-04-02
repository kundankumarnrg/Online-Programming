'''
#------------------------------------------------------------#
Question-52:
Write a Python program to compute the difference between two lists.

Input:
data1=["red", "orange", "green", "blue", "white"]
data2=["black", "yellow", "green", "blue"]

Output:
Color1-Color2:  ['red', 'white', 'orange']                                                                    
Color2-Color1:  ['black', 'yellow']

Hints:


Solution:
data1=["red", "orange", "green", "blue", "white"]
data2=["black", "yellow", "green", "blue"]

#Type-1:--------------------------------------

def find_difference(data1,data2):
    print("differnece data1 and data2")
    print(list(set(data1)-set(data2)))

    print("differnce data2 and data2")
    print(list(set(data2)-set(data1)))
find_difference(data1,data2)


#Type-2:--------------------------------------
def find_difference_data(data1,dat2):
    print("difference data1 and data2")
    lst=[]
    for val in data1:
        if val not in data2:
            lst.append(val)
    print(lst)

    print("difference data2 and data1")
    lst1=[]
    for val in data2:
        if val not in data1:
            lst1.append(val)
    print(lst1)
find_difference_data(data1,data2)


#------------------------------------------------------------#
'''



