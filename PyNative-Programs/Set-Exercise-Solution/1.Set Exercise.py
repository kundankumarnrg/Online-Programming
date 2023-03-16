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
Given a Python list, Write a program to add all its elements into a given set.

input:
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

output:
{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

Solution:
def addListElementSet(sample_set,sample_list):
    print(sample_set)
    for val in sample_list:
        sample_set.add(val)
    print(sample_set)

addListElementSet(sample_set,sample_list)

def addListElementInSet(sample_set,sample_list):
   print(sample_set)
   sample_set.update(sample_list)
   print(sample_set)

addListElementInSet(sample_set,sample_list)

#------------------------------------------------------------#



#------------------------------------------------------------#
Question-2:
Return a new set of identical items from two sets

input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output:
{40, 50, 30}

Solution:
def indenticalItems(set1,set2):
    ind_val=set()
    for val in set1:
        if val in set2:
            ind_val.add(val)
    print(ind_val)
indenticalItems(set1,set2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Write a Python program to return a new set with unique items from both sets by removing duplicates.

input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output:
{70, 40, 10, 50, 20, 60, 30}

Solution:
def uniqueItemsSet(set1,set2):
    data=set()
    for val in set1:
        data.add(val)
    
    for val in set2:
        data.add(val)
    print(data)
      
uniqueItemsSet(set1,set2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:NT
Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.



input:
set1 = {10, 20, 30}
set2 = {20, 40, 50}

output:
set1 {10, 30}

Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Write a Python program to remove items 10, 20, 30 from the following set at once.

input:
set1 = {10, 20, 30, 40, 50}

output:
{40, 50}

Solution:
def remove(set1):
    lst=[10,20,30]
    for val in lst:
        if val in set1:
            set1.remove(val)
    print(set1)
remove(set1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Return a set of elements present in Set A or B, but not both

input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output:
{20, 70, 10, 60}

Solution:
def returnElement(set1,set2):
    set_val=set()
    for val in set1:
        if val not in set2:
            set_val.add(val)

    for val in set2:
        if val not in set1:
            set_val.add(val)
    print(set_val)
returnElement(set1,set2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Check if two sets have any elements in common. If yes, display the common elements

input:
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

output:
Two sets have items in common
{10}

Solution:
def findCommanElement(set1,set2):
    com_ele=set()
    for val in set1:
        if val in set2:
            com_ele.add(val)
    print(com_ele)

findCommanElement(set1,set2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Update set1 by adding items from set2, except common items

input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output:
{70, 10, 20, 60}

Solution:
def updateSet1(set1,set2):
    set1.symmetric_difference_update(set2)
    print(set1)
        
updateSet1(set1,set2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Remove items from set1 that are not common to both set1 and set2

input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output:
{40, 50, 30}

Solution:
def removeItems(set1,set2):
    rem_val=set()
    for val in set1:
        if val not in set2:
            rem_val.add(val)

    for val in rem_val:
        set1.remove(val)
    print(set1)
removeItems(set1,set2)

#------------------------------------------------------------#


