
#------------------------------------------------------------#
Question-26:
Write a Python program to count the values associated with a key in a dictionary.

Input:
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]


Output:
Sum of id: 6
Sum of success:  2

Hints:


Solution:
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

def count_val_associated_with_key(studnet):
    sum1=0
    sum2=0
    for val in student:
        sum1=sum1+val['id']
        sum2=sum2+val['success']
    print("Sum of id:",sum1)
    print("Sum of success: ",sum2)

count_val_associated_with_key(student)

#------------------------------------------------------------#


