
#------------------------------------------------------------------------------------------#
Question-10:
Write a Python program to sum all the items in a dictionary. 

Input:
my_dict = {'data1':100,'data2':-54,'data3':247}

Output:
sum of dict value: 293

Hints:


Solution:
my_dict = {'data1':100,'data2':-54,'data3':247}

def sum_dict_val(my_dict):
    sum=0
    for val in my_dict.values():
        sum=sum+val
    print("sum of dict value:",sum)
sum_dict_val(my_dict)

#------------------------------------------------------------------------------------------#


