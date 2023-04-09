
#------------------------------------------------------------#
Question-8:
Write a Python script to merge two Python dictionaries.

Input:
dict1={"A":10,"B":20,"C":30}
dict1={"X":1000,"Y":2000,"Z":3000}

Output:
{'a': 100, 'b': 200, 'x': 300, 'y': 200}
{'a': 100, 'b': 200, 'x': 300, 'y': 200}
{'A': 10, 'B': 20, 'C': 30, 'X': 1000, 'Y': 2000, 'Z': 3000}
{'A': 10, 'B': 20, 'C': 30, 'X': 1000, 'Y': 2000, 'Z': 3000}

Hints:


Solution:
dict1={"A":10,"B":20,"C":30}
dict1={"X":1000,"Y":2000,"Z":3000}

#Type-1:-----------------------
def merze_two_dict():
    d1 = {'a': 100, 'b': 200}
    d2 = {'x': 300, 'y': 200}
    d1.update(d2)
    print(d1)
merze_two_dict()

#Type-2:-----------------------
def merze_two_dict1():
    d1 = {'a': 100, 'b': 200}
    d2 = {'x': 300, 'y': 200}
    for key,val in d2.items():
        d1[key]=val
    print(d1)
merze_two_dict1()

#Type-3:-----------------------
def merze_two_dict2():
    d1={"A":10,"B":20,"C":30}
    d2={"X":1000,"Y":2000,"Z":3000}
    dic={}
    for val in (d1,d2):
       dic.update(val)
    print(dic)
merze_two_dict2()

#Type-4:-----------------------
def merze_two_dict3():
    d1={"A":10,"B":20,"C":30}
    d2={"X":1000,"Y":2000,"Z":3000}
    dic1=d1.copy()
    dic1.update(d2)
    print(dic1)
merze_two_dict3()

#------------------------------------------------------------#




