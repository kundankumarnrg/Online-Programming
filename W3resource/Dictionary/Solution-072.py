
#------------------------------------------------------------#
Question-72:
Write a Python program to invert a dictionary with unique hashable values.

Input:
[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

Output:
{10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}

Hints:


Solution:
record=students = {
  'Theodore': 10,
  'Mathew': 11,
  'Roxanne': 9,
}

#Type-1:------------------------------
def invert_dict(record):
    dic={}
    for k,v in record.items():
        dic[v]=k
    print(dic)
invert_dict(record)

#Type-2:------------------------------
def invert_dict_record(record):
    res={val:key for key,val in record.items()}
    print(res)

invert_dict_record(record)

#------------------------------------------------------------#


