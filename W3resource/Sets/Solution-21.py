'''
#------------------------------------------------------------#
Question-21:
Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

Input:
    words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

Output:
    {'Blue': 1, 'Green': 2, 'Red': 4}

Hints:


Solution:
words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

def fequence_count(words):
    count_fre={}
    for val in set(words):
        c=0
        c=words.count(val)
        count_fre[val]=c
    print(count_fre)

fequence_count(words)

#------------------------------------------------------------#
'''


