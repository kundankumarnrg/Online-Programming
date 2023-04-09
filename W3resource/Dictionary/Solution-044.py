
#------------------------------------------------------------#
Question-44:
 Write a Python program to filter the height and width of students, which are stored in a dictionary.

Input:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height >= 6ft and Weight>=70kg:

Output:
{'Cierra Vega': (6.2, 70)}

Hints:


Solution:
dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
h=6 #ft
w=70#kg

#Type-1:------------------------------------
def fileter(dic,h,k):
    dic1={}
    for key,val in dic.items():
        height,weight=val
        if height>=h and weight>=w:
            dic1[key]=val
    print(dic1)
           
fileter(dic,h,w)

#Type-2:----------------------------------
def fileter_2(dic,h,k):
    dic1={key:val for key, val in dic.items() if val[0]>=h and val[1]>=w}
    print(dic1)
fileter_2(dic,h,w)



#------------------------------------------------------------#

