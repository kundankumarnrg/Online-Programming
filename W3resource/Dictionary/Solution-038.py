
#------------------------------------------------------------#
Question-38:
Write a Python program to match key values in two dictionaries.

Input:
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

Output:
key in both
key not in both

Hints:


Solution:
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

def check_key_both(x,y,key):
    lst1=list(x.keys())
    lst2=list(y.keys())
    print("key in both" if(key in lst1 and lst2) else "key not in both ")

check_key_both(x,y,key="key1")
check_key_both(x,y,key='key5')

#------------------------------------------------------------#


