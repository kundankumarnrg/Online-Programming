'''
#------------------------------------------------------------#
Question-28:
Write a Python program to find the second largest number in a list.

Input:
[1, 2, -8, -2, 0, -2]
[1, 1, 1, 0, 0, 0, 2, -2, -2]
[2,2]

Output:
1
1
1
2
2

Hints:


Solution:
def second_largest_number_list(lst):
    val=list(sorted(set(lst)))
    l=len(val)
    if len(val)>=2:
        return val[l-2]
    else:
        return val[l-1]

print(second_largest_number_list([1, 2, -8, -2, 0, -2]))
print(second_largest_number_list([1, 1, 0, 0, 2, -2, -2]))
print(second_largest_number_list([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_largest_number_list([2,2]))
print(second_largest_number_list([2]))

#------------------------------------------------------------#
'''
