
#------------------------------------------------------------#
Question-6:
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

Input:
num=10

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

Hints:


Solution:
num=10

def genrate_dict(num):
    dic={}
    for i in range(1,num):
        dic[i]=i*i
    print(dic)
        
genrate_dict(num)

#------------------------------------------------------------#





