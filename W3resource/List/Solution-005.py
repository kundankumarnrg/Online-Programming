'''
#------------------------------------------------------------#
Question-5:
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

input:
sample_list = ['abc', 'xyz', 'aba', '1221','121']

output:
Expected Result:  3

Hints:


Solution:

sample_list = ['abc', 'xyz', 'aba', '1221','121']
def count_number_string(sample_list,num):
    c=0
    for val in sample_list:
        if len(val)>num:
            if val[0]==val[-1]:
                c=c+1
    print("Expected Result: ",c)

num=2
count_number_string(sample_list,num)

#------------------------------------------------------------#
'''

