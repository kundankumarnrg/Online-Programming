
#------------------------------------------------------------#
Question-1:
Write a Python script to add a key to a dictionary.

Input:
dic={0: 10, 1: 20}
dic1={0: 10, 1: 20, 3: 30}
Output:
{0: 10, 1: 20, 3: 30}
{0: 10, 1: 20, 3: 30, 4: 40}
Hints:
dic.update()

Solution:
dic={0: 10, 1: 20}

#Type-1:-------------------------------
def add_key_val(dic):
    print(dic)
    dic[3]=30
    print(dic)
add_key_val(dic)

#Type-2:------------------------------
def update_val(dic):
    print(dic)
    dic.update({4:40})
    print(dic)
update_val(dic)

#------------------------------------------------------------#





