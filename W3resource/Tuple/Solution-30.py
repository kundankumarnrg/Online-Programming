'''
#------------------------------------------------------------#
Question-:
Write a Python program to check if a specified element appears in a tuple of tuples.

Input:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

Output:
Present

Hints:


Solution:
t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

def check_val_present_not(t,val):
    a,b,c=t
    print("Present" if val in a or b or c else "Not Present")
check_val_present_not(t,'redd')

#------------------------------------------------------------#
'''

