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
Write a program to create a function that takes two arguments, name and age, and print their value.

input:


output:


Solution:
#----------------without argument---------
def show():
    print("Hello function...!")

show()


#----------with argument----------------
def showOne(roll,name):
    print("Roll no:",roll)
    print("Name:",name)

showOne(101,"kundan")

#------------------------------------------------------------#



#------------------------------------------------------------#
Question-2:
Write a program to create function func1() to accept a variable length of arguments and print their value.

input:
# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)

output:
Printing values
20
40
60


Printing values
80
100

Hints:
Create a function in such a way that we can pass any number of arguments 
to this function, and the function should process them and display each 
argument’s value.

Solution:
#--------------three argument------------
def fun1(*args):
    for val in args:
        print(val)

fun1(10,20,30)
fun1(100,200)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Write a program to create function calculation() such that it can accept 
two variables and calculate addition and subtraction. Also, it must return 
both addition and subtraction in a single return call.

input:
def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)

output:
50, 30

Solution:
def calculation(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return add, sub, mul, div

val=calculation(20,5)
for res in val:
    print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Write a program to create a function show_employee() using the following conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary

input:
showEmployee("Ben", 12000)
showEmployee("Jessa")

output:
Name: Ben salary: 12000
Name: Jessa salary: 9000

Solution:
def showDefValues(name='kundan',location="delhi"):
    print("Name:",name)
    print("Location:",location)


showDefValues("vishal",'pune') 

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it

input:


output:


Solution:
def OuterFuncation(a,b):
    def innerFunction(m,n):
        add=m+n
        return add
    
    res=innerFunction(a,b)
    res=res+100
    print(res)
        
OuterFuncation(10,20)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

input:
0-10.

output:
55

Hints:
A recursive function is a function that calls itself again and again.

Solution:
def recursiveFun(num):
    if num>0:
        return num+recursiveFun(num-1)
    else:
        return 0
res = recursiveFun(10)
print(res)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name

input:
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

output:
show_student(name, age)

Solution:
def represent(name,location):
    print("Name: ",name)
    print("Location:",location)


represent('premvardhan','bangalore')
show=represent
show('vishal','pune')

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Generate a Python list of all the even numbers between 4 to 30

input:


output:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

Solution:
def genEvenNumList():
    lst=list(range(4,31,2))
    print(lst)
genEvenNumList()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Find the largest item from a given list

input:
x = [4, 6, 8, 24, 12, 2]

output:
24

Solution:
def maxEelement(lst):
    print("Max element of list: ",max(lst))

lst=[4, 6, 8, 24, 12, 2]
maxEelement(lst)

#------------------------------------------------------------#







