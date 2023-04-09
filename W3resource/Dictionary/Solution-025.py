
#------------------------------------------------------------#
Question-25:
Write a Python program to print a dictionary in table format.

Input:
dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

Output:
C1	C2	C3	
1	2	3	
5	6	7	
9	10	11	

Hints:


Solution:
dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

def dict_into_tabl_format(dic):
    for key in dic:
        print(key,end="\t")
    print()
    
    for val in dic.values():
        for v in val:
            print(v,end="\t")
        print()

dict_into_tabl_format(dic)

#------------------------------------------------------------#


