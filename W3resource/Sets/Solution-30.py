'''
#------------------------------------------------------------#
Question-30:
Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.

Input:
lst=['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
lst=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']

Output:
{'abc', 'qux', 'baz', 'foo', 'bar'}
{'Exercises', 'Python', 'Practice', 'Solution'}

Hints:


Solution:
lst=['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']

def remove_duplicate_val(lst):
    print(lst)
    uni_val=set(lst)
    return uni_val
print(remove_duplicate_val(lst))
print(remove_duplicate_val(lst=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']))


#------------------------------------------------------------#
'''
