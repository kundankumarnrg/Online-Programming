
#------------------------------------------------------------#
Question-63:
Write a Python program to convert a given list of lists to a dictionary.

Input:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

Output:
Convert the said list of lists to a dictionary:
{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

Hints:


Solution:
giv_data=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

def convert_list_into_dict(giv_data):
    dic={}
    for val in giv_data:
        tem=[]
        for i in range(1,len(val)):
            tem.append(val[i])
        dic[val[0]]=tem
    print(dic)

convert_list_into_dict(giv_data)

#------------------------------------------------------------#


