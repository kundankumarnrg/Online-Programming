'''
#------------------------------------------------------------#
Question-27:
Write a Python program to find the second smallest number in a list.

Input:
[1, 2, -8, -2, 0, -2]
[1, 1, 1, 0, 0, 0, 2, -2, -2]
[2,2]

Output:
-2
0
0
2
2

Hints:


Solution:
def second_samllest_number_list(lst):
    val=list(sorted(set(lst)))
    if len(val)>=2:
        return val[1]
    else:
        return val[0]

print(second_samllest_number_list([1, 2, -8, -2, 0, -2]))
print(second_samllest_number_list([1, 1, 0, 0, 2, -2, -2]))
print(second_samllest_number_list([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_samllest_number_list([2,2]))
print(second_samllest_number_list([2]))

#------------------------------------------------------------#
'''
