
#------------------------------------------------------------#
Question-45:
Write a Python program to verify that all values in a dictionary are the same.

Input:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.

Output:
True
False

Hints:


Solution:
dic={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
num=12
num1=10

#Type-1:--------------------------------------
def varify_all_dic_val(dic,num):
    for val in dic.values():
        if num!=val:
            return ("False")
            break
        else:
            return ("True")

print(varify_all_dic_val(dic,num))
print(varify_all_dic_val(dic,num1))

#Type-2:--------------------------------------
def varify_all_dict_value_1(dic,num):
    c=0
    lst=list(dic.values())
    for v in lst:
        if v==num:
            c=c+1
    print("True" if (len(lst))==c else "False")


varify_all_dict_value_1(dic,num)
varify_all_dict_value_1(dic,num1)

#------------------------------------------------------------#








