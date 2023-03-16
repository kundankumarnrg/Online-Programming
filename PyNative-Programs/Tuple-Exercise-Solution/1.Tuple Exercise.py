#============================================================================================
>>Formate:
1.Question
2.Input
3.Output
4.Hints
5.Solution
#============================================================================================

#------------------------------------------------------------#
Question-1:
 Reverse the tuple

input:
tuple1 = (10, 20, 30, 40, 50)

output:
(50, 40, 30, 20, 10)

Solution:
def reverseTuple(tuple1):
    print(tuple1)
    print(tuple1[::-1])
reverseTuple(tuple1)
'''

'''
#Type-2:-----------------------------
def reverseTuple(tuple1):
    print(tuple1)
    for i in range(len(tuple1)-1,-1,-1):
        print(tuple1[i],end=", ")
reverseTuple(tuple1)
'''
'''
#Type-3:------------------------------
def reverseTuple(tupple1):
    print(tuple1)
    t=tuple(reversed(tuple1))
    print(t)
reverseTuple(tuple1)

#------------------------------------------------------------#



#------------------------------------------------------------#
Question-2:
The given tuple is a nested tuple. write a Python program to print the value 20.

input:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

output:
20

Solution:
def accessElement(tuple1):
    print(tuple1)
    print(tuple1[1][1])

accessElement(tuple1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Create a tuple with single item 50

input:


output:


Solution:
def createTuple():
    t=50,
    print(t)
    print(type(t))
createTuple()
'''
'''
#Type-2:-------------------------------------
def createTuple():
    t=(50,)
    print(t)
    print(type(t))
createTuple()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Write a program to unpack the following tuple into four variables and display each variable.

input:
tuple1 = (10, 20, 30, 40)

output:
tuple1 = (10, 20, 30, 40)
# Your code
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40

Solution:
def unpackTuple(tuple1):
    a,b,c,d=tuple1
    print('a:',a,'\nb:',b,'\nc:',c,'\nd:',d)

unpackTuple(tuple1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Swap two tuples in Python

input:
tuple1 = (11, 22)
tuple2 = (99, 88)

output:
tuple1: (99, 88)
tuple2: (11, 22)

Solution:
def swapTwoTuple(tuple1,tuple2):
    print('Tuple1:',tuple1,'\nTuple2:',tuple2)
    tuple1,tuple2=tuple2,tuple1
    print('\nTuple1:',tuple1,'\nTuple2:',tuple2)
    
swapTwoTuple(tuple1,tuple2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

input:
tuple1 = (11, 22, 33, 44, 55, 66)

output:
tuple2: (44, 55)

Solution:
def copySpecficElement(tuple):
    print(tuple1)
    print("Coply Elements")
    t=tuple1[0:3]
    print(t)
copySpecficElement(tuple1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

input:
tuple1 = (11, [22, 33], 44, 55)

output:
tuple1: (11, [222, 33], 44, 55)

Solution:
def modifiyTuple(tuple1):
    print(tuple1)
    tuple1[1][0]=222
    print(tuple1)
modifiyTuple(tuple1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Sort a tuple of tuples by 2nd item

input:
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

output:
(('c', 11), ('a', 23), ('d', 29), ('b', 37))

Solution:
def SortTuple(tuple1):
    print(tuple1)
    tuple1=tuple(sorted(list(tuple1),key=lambda x:x[1]))
    print(tuple1)
SortTuple(tuple1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Counts the number of occurrences of item 50 from a tuple

input:
tuple1 = (50, 10, 60, 70, 50)

output:
2


Solution:
def countVal(tuple):
    val=50
    print(tuple1.count(val))

countVal(tuple1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Check if all items in the tuple are the same

input:
tuple1 = (45, 45, 45, 45)

output:
True

Solution:
def checkAllEleSame(tuple1):
    tem=tuple1[0]
    c=0
    for val in tuple1:
        if val==tem:
            c=c+1
    print("True" if(c==len(tuple1)) else "False")
checkAllEleSame(tuple1)

#------------------------------------------------------------#



