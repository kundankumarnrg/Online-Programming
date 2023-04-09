
#------------------------------------------------------------#
Question-19:
Write a Python program to combine two dictionary by adding values for common keys. 

Input:
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

Output:
({'a': 400, 'b': 400, 'd': 400, 'c': 300})

Hints:


Solution:
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

from collections import Counter
def combine_two_dict(d1,d2):
    res=Counter(d1)+Counter(d2)
    print(res)
    
combine_two_dict(d1,d2)


#------------------------------------------------------------#


