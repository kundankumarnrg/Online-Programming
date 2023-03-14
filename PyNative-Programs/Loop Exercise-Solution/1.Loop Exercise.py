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
Print First 10 natural numbers using while loop

input:
val=10

output:
1,2,3,4,5,6,7,8,9,10

Solution:
#------------Type-1-------------------------#
def print_Natural_Number(num):
    for i in range(1,num+1):
        print(i)

print_Natural_Number(10)


#------------Type-2-------------------------#
def print_Natural_Number1(num1):
    i=1
    while(i<=num1):
        print(i)
        i=i+1
print_Natural_Number1(10)


#------------------------------------------------------------#



#------------------------------------------------------------#
Question-2:
Print the following pattern

input:
val=5

output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

Solution:
def print_Pattern(val):
    for i in range(1,val+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
print_Pattern(5)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
 Calculate the sum of all numbers from 1 to a given number.

input:
given_no=10

output:
Sum is:  55

Solution:
def sum_All_Number(giv_num):
    sum=0
    for val in range(giv_num+1):
        sum=sum+val
    print("calculate all number:",sum)
    
sum_All_Number(10)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Write a program to print multiplication table of a given number.

input:
num=5

output:


Solution:
def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)   
table(2)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

input:
[12, 75, 150, 180, 145, 525, 50]

output:
75,150,145

Solution:
def dip_List(number):
    for val in number:
        print(val)
number = [12, 75, 150, 180, 145, 525, 50]
dip_List(number)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Write a program to count the total number of digits in a number using a while loop.

input:
75869

output:
5

Solution:
#------------------------Type-1---------------------------------
def count_Digits(num):
    c=0
    while(num>0):
        rem=num%10
        c=c+1
        num=num//10
    print(c)

count_Digits(7586956)


#------------------------Type-2---------------------------------
def count_Digits1(num):
    str1=str(num)
    print(len(str1))

count_Digits1(7586956)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Write a program to use for loop to print the following reverse number pattern.

input:
num=5

output:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

Solution:
def print_pattern(val):
    for i in range(val,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print();

print_pattern(5)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Print list in reverse order using a loop

input:
list1 = [10, 20, 30, 40, 50]

output:
[50,40,30,20,10]

Solution:
def reverse_Order_List(lst):
    for val in lst[::-1]:
        print(val)

lst= [10, 20, 30, 40, 50]
reverse_Order_List(lst)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Display numbers from -10 to -1 using for loop.

input:


output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1

Solution:
def dip_Number():
    for i in range(-10,0,1):
        print(i)
dip_Number()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Use else block to display a message “Done” after successful execution of for loop.

input:
For example, the following loop will execute without any error.
for i in range(5):
    print(i)
    
output:
0
1
2
3
4
Done!

Solution:

def print_val():
    for i in range(5):
        print(i)
    else:
        print("Done...!")

print_val()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-11:
Write a program to display all prime numbers within a range.

input:
start = 25
end = 50

output:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47

Solution:
def prime_Num_Range(start, end):
    for val in range(start,end+1):
        c=0
        for i in range(1,val+1):
            if(val%i==0):
                c=c+1
        if c==2:
            print(val)

prime_Num_Range(25,50)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-12:
Display Fibonacci series up to 10 terms

input:
num=10

output:
0  1  1  2  3  5  8  13  21  34

Hints:
The Fibonacci Sequence is a series of numbers. The next number is found 
by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series 
above is 13+21 = 34.

Solution:
def fibonacci_Series(term):
    f,s=0,1
    for i in range(term):
        print(f,end=", ")
        f,s=s,f+s
fibonacci_Series(10)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-13:
Write a program to use the loop to find the factorial of a given number.

input:
num=5

output:
res= 5 × 4 × 3 × 2 × 1 = 120

Hints:
The factorial (symbol: !) means to multiply all whole numbers from the 
chosen number down to 1.

For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120

Solution:
def fact_Number(num):
    fact=1
    while(num>0):
        fact=fact*num
        num=num-1
    print(fact)
fact_Number(5)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-14:
Reverse a given integer number

input:
76542

output:
24567

Solution:
#-------------------------Type-1-------------------
def reverse_Int_Val(num):
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)

reverse_Int_Val(76542)

#-------------------------Type-2-------------------

def reverse_Int_Val1(num):
    str_val=str(num)
    print(int(str_val[::-1]))

reverse_Int_Val1(76542)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-15:
Use a loop to display elements from a given list present at odd index positions.

input:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

output:
20 40 60 80 100

Solution:
def print_Odd_Possition_val(lst):
    for i in range(len(lst)):
        if(i%2!=0):
            print(lst[i],end=" ")

lst=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print_Odd_Possition_val(lst)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-16:
Write a program to rint the cube of all numbers from 1 to a given number.

input:
number = 6

output:
Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216

Solution:
def cube_Given_Number(giv_num):
    for i in range(1,giv_num+1):
        print(i,"and the cube: ",(i*i*i))

cube_Given_Number(10)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-17:
Write a program to calculate the sum of series up to n term. For example, 
if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

input:
n=5

output:
24690

Solution:
def Sum_Series(num,term):
    sum,add=0,0
    for i in range(1,term+1):
        sum=sum*10+num
        add=add+sum
    print(add)


Sum_Series(2,5)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-18:
Write a program to print the following start pattern using the for loop.

input:


output:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

Solution:
def print_Pattern(term):
    for i in range(term):
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(term-1,-1,-1):
        for j in range(i,-1,-1):
            print("*",end=" ")
        print()

print_Pattern(5)

#------------------------------------------------------------#










