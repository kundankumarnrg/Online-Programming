'''
#------------------------------------------------------------#
Question-24:
Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

Input:
    lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]

Output:
    {8, 9}

Hints:


Solution:
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def maximum_product_among_all_pairs(lst):
    tem=1
    for i in range(len(lst)):
        s=set()
        for j in range(i+1,len(lst)):
            if (((lst[i])*(lst[j]))>tem):
                s=set([lst[i],lst[j]])
                tem=lst[i]*lst[j]
                s1=s
    print(s1)
        
maximum_product_among_all_pairs(lst)

#------------------------------------------------------------#
'''
