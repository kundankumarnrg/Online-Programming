
#------------------------------------------------------------#
Question-13:
Write a Python program to map two lists into a dictionary. 

Input:
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

Output:
{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
Hints:


Solution:
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

#Type-1:------------------------------------
def map_list(keys,values):
    dic={}
    for i in range(len(keys)):
        dic[(keys[i])]=values[i]
    print(dic)
    
map_list(keys,values)


#Type-2:------------------------------------
def map_list(keys,values):
    res=dict(zip(keys,values))
    print(res)
map_list(keys,values)


#------------------------------------------------------------#



