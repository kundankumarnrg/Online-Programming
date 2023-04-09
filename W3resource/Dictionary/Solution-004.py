
#------------------------------------------------------------#
Question-4:
Write a Python script to check whether a given key already exists in a dictionary.

Input:
dic= {10: 1, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Output:
False
True
Not Present
Present
Present
Not Present

Hints:


Solution:
dic= {10: 1, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#Type-1:-----------------------------
def find_key_in_dict(dic,key):
    f=0
    for k in dic.keys():
        if k==key:
            f=1
            break
    print("True" if f==1 else "False")
        
find_key_in_dict(dic,key=51)
find_key_in_dict(dic,key=6)


#Type-2:---------------------------
def find_key_dict(dic,k):
    print("Present" if k in dic else "Not Present" )

find_key_dict(dic,k=1)
find_key_dict(dic,k=10)


#Type-3:--------------------------
def find_key_dict1(dic,k):
    lst=[]
    lst=dic.keys()
    print("Present" if k in lst else "Not Present")

find_key_dict1(dic,k=2)
find_key_dict1(dic,k=11)

#------------------------------------------------------------#


