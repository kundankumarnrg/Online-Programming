
#------------------------------------------------------------#
Question-61:
Write a Python program to count the frequency of a dictionary.

Input:
{'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

Output:
Count the frequency of the said dictionary:
Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

Hints:


Solution:
simple_val={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

def frequencey_val(simple_val):
    print(simple_val)
    res={}
    c=0
    val=list(simple_val.values())
    for v in (set(val)):
        c=0
        c=val.count(v)
        res[v]=c
    print(res)


frequencey_val(simple_val)

#------------------------------------------------------------#


