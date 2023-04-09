
#------------------------------------------------------------#
Question-42:
Write a Python program to filter a dictionary based on values. 

Input:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:

Output:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

Hints:


Solution:
dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
mark=170

#Type-1:--------------------------
def fileter_dic(dic,mark):
    print(dic)
    dic1={}
    for k,v in dic.items():
        if v>mark:
            dic1[k]=v
    print(dic1)
fileter_dic(dic,mark)


#Type-2:--------------------------
def filter_dict(dic,mark):
    print(dic)
    res={k:v for k,v in dic.items() if v>mark}
    print(res)
filter_dict(dic,mark)

#------------------------------------------------------------#


