'''
#------------------------------------------------------------#
Question-26:
Write a Python program to calculate the product, multiplying all the numbers in a given tuple.

Input:
(4, 3, 2, 2, -1, 18)
(2, 4, 8, 8, 3, 2, 9)

Output:
-864
27648

Hints:


Solution:
def product_all_ele(t):
    prod=1
    for val in t:
        prod=prod*val
    return prod

print(product_all_ele((4, 3, 2, 2, -1, 18)))
print(product_all_ele((2, 4, 8, 8, 3, 2, 9)))

#------------------------------------------------------------#
'''

