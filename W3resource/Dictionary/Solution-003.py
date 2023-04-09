
#------------------------------------------------------------#
Question-3:
Write a Python script to concatenate the following dictionaries to create a new one.

Input:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

Output:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Hints:


Solution:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

def concatenate_dict(dic1,dic2,dic3):
    res={}
    print("\n",dic1,"\n",dic2,"\n",dic3)
    for val in (dic1,dic2,dic3):
        res.update(val)
    print(res)
concatenate_dict(dic1,dic2,dic3)


#------------------------------------------------------------#




