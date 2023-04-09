
#------------------------------------------------------------#
Question-17:
 Write a Python program to remove duplicates from the dictionary.

Input:
data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

Output:
{'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 
'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}}


Hints:


Solution:
data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

def remove_duplicate_val(data):
    dic={}
    print(data)
    for key,val in data.items():
        if val not in dic.values():
            dic[key]=val
    print(dic)
remove_duplicate_val(data)

#------------------------------------------------------------#


