
#------------------------------------------------------------#
Question-31:
Write a Python program to get the key, value and item in a dictionary. 

Input:
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Output:
keys	values	Count
1 	 10 	 1
2 	 20 	 2
3 	 30 	 3
4 	 40 	 4
5 	 50 	 5
6 	 60 	 6

Hints:


Solution:
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def show_key_value_count(dict_num):
    c=0
    print("keys\tvalues\tCount")
    lst=list(dict_num.values())
    for key,val in dict_num.items():
        c=c+1
        print(key,"\t",val,"\t",c)

show_key_value_count(dict_num)

#------------------------------------------------------------#


