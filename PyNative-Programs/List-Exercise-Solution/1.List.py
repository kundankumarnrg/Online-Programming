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
Reverse a list in Python

input:
list1 = [100, 200, 300, 400, 500]

output:
[500, 400, 300, 200, 100]

Solution:
#-----------------------Type-1---------------------------------
def reverseList(lst):
    print(list(reversed(lst)))


lst=[100, 200, 300, 400, 500]
reverseList(lst)



#----------------------------Type-2-----------------------------
def revWithSlicing(lst):
    print(lst[::-1])

lst=[100, 200, 300, 400, 500]
revWithSlicing(lst)




#----------------------------Type-3---------------------------
def revList(lst):
    rev_list=[]
    for i in range((len(lst))-1,-1,-1):
        rev_list.append(lst[i])
    print(rev_list)
        

lst=[100, 200, 300, 400, 500]
revList(lst) 

#------------------------------------------------------------#



#------------------------------------------------------------#
Question-2:
Write a program to add two lists index-wise. Create a new list that 
contains the 0th index item from both the list, then the 1st index item, 
and so on till the last element. any leftover items will get added at the 
end of the new list.

input:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

output:
['My', 'name', 'is', 'Kelly']

Solution:
def concatinate_Two_List_Index_Wise(l1,l2):
    new_List=[]
    for i in range(len(l1)):
        tem=""
        tem=l1[i]+l2[i]
        new_List.append(tem)
    print(new_List)


l1 = ["M", "na", "i", "Ke"]
l2 = ["y", "me", "s", "lly"]
concatinate_Two_List_Index_Wise(l1,l2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Given a list of numbers. write a program to turn every item of a list into its square.

input:
numbers = [1, 2, 3, 4, 5, 6, 7]

output:
[1, 4, 9, 16, 25, 36, 49]

Solution:
#-----------------------Type-1------------------------------------
def squareListElement(lst):
    sqr_list=[]
    for val in lst:
        tem=1
        tem=val*val
        sqr_list.append(tem)
    print(sqr_list)

lst=[1, 2, 3, 4, 5, 6, 7]
squareListElement(lst)


#-----------------------Type-2-----------------------------------
def squareListEle(l1):
    output=list(i*i for i in l1)
    print(output)

l1=[1, 2, 3, 4, 5, 6, 7]
squareListEle(l1)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Concatenate two lists in the following order

input:
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

Solution:
def concatenate(l1,l2):
    new_lst=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            tem=""
            tem=l1[i]+l2[j]
            new_lst.append(tem)       
    print(new_lst)

l1 = ["Hello ", "take "]
l2 = ["Dear", "Sir"]
concatenate(l1,l2)
#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:NT
Given a two Python list. Write a program to iterate both lists 
simultaneously and display items from list1 in original order and items 
from list2 in reverse order.

input:
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

output:
10 400
20 300
30 200
40 100

Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Remove empty strings from the list of strings

input:
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

output:
["Mike", "Emma", "Kelly", "Brad"]

Solution:
def removeEmptyEle(list1):
    for val in list1:
        if val==" " or val=="":
            list1.remove(val)
    print(list1)


list1=["Mike", "", "Emma", "Kelly", "", "Brad"]
removeEmptyEle(list1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Write a program to add item 7000 after 6000 in the following Python List

input:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

Solution:
def addItems(lst):
    print("Befor add Item list:",lst)
    lst[2][2].append(700)
    print("After adding list:",lst)


lst= [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
addItems(lst)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
You have given a nested list. Write a program to extend it by adding the 
sublist ["h", "i", "j"] in such a way that it will look like the following 
list.

input:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

Solution:
def addNestedList(list1,sub_list):
    list1[2][1][2].extend(sub_list)
    print(list1)

list1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list=["h", "i", "j"]
addNestedList(list1,sub_list)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
You have given a Python list. Write a program to find value 20 in the list,
and if it is present, replace it with 200. Only update the first 
occurrence of an item.

input:
list1 = [5, 10, 15, 20, 25, 50, 20]

output:
[5, 10, 15, 200, 25, 50, 20]

Solution:
def updateElement(l1):
    for i in range(len(l1)):
        if l1[i]==20:
            l1.remove(l1[i])
            l1.insert(i,200)
            break
    print(l1)

l1 = [5, 10, 15, 20, 25, 50, 20]
updateElement(l1)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Given a Python list, write a program to remove all occurrences of item 20.

input:
list1 = [5, 20, 15, 20, 25, 50, 20]

output:
[5, 15, 25, 50]

Solution:
def removeEle(lst):
    for val in lst:
        if val==20:
            lst.remove(val)
    print(lst) 
    
lst=[5, 20, 15, 20, 25, 50, 20]
removeEle(lst)


#------------------------------------------------------------#


