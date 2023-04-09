
#------------------------------------------------------------#
Question-57:
Write a Python program to filter even numbers from a dictionary of values.

Input:
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

Output:
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]}

Hints:


Solution:
dic_val={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic_val2={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
def filter_evne_val_dic(dic_val):
    tem=[]
    dic={}
    for k,v in dic_val.items():
        tem=[]
        for l_val in v:
            if l_val%2==0:
                tem.append(l_val)
        dic[k]=tem
    print(dic)

filter_evne_val_dic(dic_val)
filter_evne_val_dic(dic_val2)

#------------------------------------------------------------#




