'''
#------------------------------------------------------------#
Question-12:
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

Input:
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
removing the 0th, 4th and 5th elements.

Output:
res=['Green', 'White', 'Black']

Hints:


Solution:
sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#removing 0th,4th, 5th possition element

def remove_spefic_element(sample_list):
    print(sample_list)
    rem_ele=[5,4,0]
    for val in rem_ele:
        sample_list.remove(sample_list[val])
        
    print(sample_list)
remove_spefic_element(sample_list)

#------------------------------------------------------------#
'''

