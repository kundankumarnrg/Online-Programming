
#------------------------------------------------------------#
Question-75:
Write a Python program to find all keys in a dictionary that have the given value. 

Input:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

Output:
Find all keys in the said dictionary that have the specified value:
['Roxanne', 'Betty]

Hints:


Solution:
record= {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}
giv_val=20

#Type-1:---------------------------------
def find_all_key_dict(record,giv_val):
    lst=[]
    for key,val in record.items():
        if val==giv_val:
            lst.append(key)
    print(lst)
            
find_all_key_dict(record,giv_val)

#Type-2:---------------------------------
def find_all_key_dict(record,giv_val):
    res=[key for key,val in record.items() if giv_val==val]
    print(res)            
find_all_key_dict(record,giv_val)

#------------------------------------------------------------#


