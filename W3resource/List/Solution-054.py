'''
#------------------------------------------------------------#
Question-54:
Write a Python program to concatenate elements of a list.

Input:
color = ['red', 'green', 'orange']

Output:
red-green-orange                                                                                              
redgreenorange

Hints:


Solution:
lst = ['red', 'green', 'orange']

#Type-1:-------------------------

def cancatinate_list_ele(lst):
    print(lst)
    print('-'.join(lst))
    print(" ".join(lst))

cancatinate_list_ele(lst)



#Type-2:-------------------------
def cancatinate_list_ele(lst):
    str1=""
    str2=""
    for val in lst:
        str1=str1+val+"_"
        str2=str2+val
    print(str1.strip("_"))
    print(str2)

cancatinate_list_ele(lst)

#------------------------------------------------------------#
'''


