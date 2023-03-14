#============================================================================================
>>Formate:
1.Question
2.Input
3.Output
4.Hints
5.Solution
#============================================================================================
#------------------------------------------------------------#
Question-1:
Calculate the multiplication and sum of two numbers.

input:
number1 = 20
number2 = 30

number1 = 40
number2 = 30

output:
result is 600
result is 70

Solution:
#------------------------Addition two number----------------------
def add_Tow_Number():
    print("sum of two number:",(int(input("enter first number: ")))+(int(input("Enter second number: "))))
add_Tow_Number()


#----------------------Multiplication two number-------------------
def mul_Two_Number():
    print("Multiplication two:",(int(input("\nEnter first number: ")))*(int(input("Enter second number: "))))

mul_Two_Number()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-2:
Print the sum of the current number and the previous number.

input:
num=10

output:
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17

Solution:
def sum_cunrent_privious_Number(term):
    pre=0
    for i in range(term+1):
        print("current number:",i,"Privious Number:",pre,"sum:",(i+pre))
        pre=i
num=int(input("Please Enter number: "))
sum_cunrent_privious_Number(num)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Print characters from a string that are present at an even index number.

input:
str = "PythonProgramList"

output:
PtoPormit

Solution:
def print_Even_Position_index_char(str_val):
    for i in range(len(str_val)):
        if i%2==0:
            print(str_val[i],end="")

str_val="PythonProgramList"
print_Even_Position_index_char(str_val)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Remove first n characters from a string.
Write a program to remove characters from a string starting from zero up to n and return a new string.
input:
str_val="pynative"
n=4
output:
res=onCode

Solution:
def remove_NCharacter(n,str_val):
    print(str_val[n+1::])

remove_NCharacter(3,"pythonCode")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Check if the first and last number of a list is the same

input:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

output:
True
False

Solution:
def fist_Last_Element_Same(lst1):
    print("First & last same" if (lst1[0]==lst1[-1]) else "not same")

lst1=[10, 20, 30, 40, 10]
lst1=[75, 65, 35, 75, 30]
fist_Last_Element_Same(lst1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Display numbers divisible by 5 from a list.

input:
[10, 20, 33, 46, 55]

output:
10 20 55

Solution:
def div_by_five(lst):
    for val in lst:
        if val%n==0:
            print(val, end=" ")


lst=[10,20,15,17,18,25,36]
n=5
div_by_five(n,lst)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Return the count of a given substring from a string.

input:
str_val="python is good programming language. python is easy and user friendly"
sub_val="is"

output:
is appeared 2 times

Solution:
def ocurre_Sub_String(str_val,sub_str_val):
    print(sub_str_val,"occure",str_val.count(sub_str_val))

str_val="python is good programming language. python is easy and user friendly"
sub_str_val="is"
ocurre_Sub_String(str_val,sub_str_val)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Print the following pattern

input:
num=5

output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

Solution:
def print_Pattern(num):
    for i in range(1,num+1):
        for j in range(i):
            print(i,end=" ")
        print()
num=5
print_Pattern(num)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Check Palindrome Number.

input:
number 121
number 125

output:
palindrome number
Not palindrome number

Solution:
def palindrom_Number(num):
    cp=num
    rem,pl=0,0
    while(num>0):
        rem=num%10
        pl=pl*10+rem
        num=num//10
    print("palindrom number" if(cp==pl) else "Not palindrom")

num=121
num=123
palindrom_Number(num)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Create a new list from a two list using the following condition
Given a two list of numbers, write a program to create a new list 
such that the new list should contain odd numbers from the first 
list and even numbers from the second list.

input:
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [11,12,13,14,15,16,17,18,19,20]
output:
result list: [2, 4, 6, 8, 10, 11, 13, 15, 17, 19]
Solution:
def list_Odd_Even(lst1,lst):
    output=[]
    for val in lst1:
        if val%2==0:
            output.append(val)

    for val in lst2:
        if val%2!=0:
            output.append(val)
    print(output)


lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [11,12,13,14,15,16,17,18,19,20]
list_Odd_Even(lst1,lst2)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-11:
Write a Program to extract each digit from an integer in the reverse order.

input:
If the given int is 7536, the output shall be “6 3 5 7

output:
 6357

Solution:
def extract_Digits_Reverse(num):
    print("Number is: ",num)
    rev,rem=0,0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print("After extracting reverse Number: ",rev)

extract_Digits_Reverse(7536)

#------------------------------------------------------------#

#------------------------------------------------------------#
Question-12:


input:


output:


Solution:


#------------------------------------------------------------#

#------------------------------------------------------------#
Question-13:
Print multiplication table form 1 to 10.

input:


output:
1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 

Solution:
def print_Table(f_range,s_range):
    for val in range(f_range,s_range+1):
        for i in range(1,10+1):
            print(val*i,end=" ")
        print()

print_Table(1,10)

#------------------------------------------------------------#

#------------------------------------------------------------#
Question-14:
Print downward Half-Pyramid Pattern with Star (asterisk).

input:


output:
* * * * *  
* * * *  
* * *  
* *  
*

Solution:
def half_pyramid_pattern(num):
    for i in range(num,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()
        
half_pyramid_pattern(5)

#------------------------------------------------------------#

#------------------------------------------------------------#
Question-15:
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

input:
Case-1:
base = 2
exponent = 5

Case-2:
base = 5
exponent = 4

output:
case-1:
2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

case-2:
5 raises to the power of 4 is: 625 i.e (5 *5 * 5 *5 = 625)

Solution:
def exp_val(base,exp):
    output=1
    while(exp>0):
        output=output*base
        exp=exp-1
    print(output)


exp_val(2,5)

#------------------------------------------------------------#


