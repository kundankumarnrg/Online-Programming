
#------------------------------------------------------------#
Question-71:
Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.

Input:


Output:
Russell
2

Hints:


Solution:
users = {
  'Carla': {
    'name': {
      'first': 'Carla ',
      'last': 'Russell' 
    },
    'postIds': [1, 2, 3, 4, 5]
  }
}

def access_nested_dict_key(users):
    print(users['Carla']['name']['last'])
    print(users['Carla']['postIds'][1])
access_nested_dict_key(users)


#------------------------------------------------------------#


