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
Accept numbers from a user.

input:
int values
string values
boolean values
float values

output:
res=10
str_val="python"
bol=True
f1=10.2

Solution:
#---------------input String val-----------
name=input("please enter you name: ")
email=input("Please enter your email: ")
print("User name: ",name,"and user email id: ",email)


#---------------Input Integer val---------
phone_no=int(input("Please enter you mobile number: "))
pincode=int(input("Please enter pincode: "))

print("user name: ",name)
print("user email id: ",email)
print("user phone number: ",phone_no)
print("user pincode: ",pincode)

#------------------------------------------------------------#



#------------------------------------------------------------#
Question-2:
Display Some format.

input:
str1='Name' 'Is' 'James'

output:
res= Name**Is**James

Solution:
#Type-1:-----------------------------------#
def formateOutput():
    str1=input("Please enter value:")
    val1=str1.replace(" ","**")
    val2=val1.replace("'","")
    val3=val2.replace(",","")
    print(val3)
formateOutput()

#Type-2:----------------------------------#
print('My', 'Name', 'Is', 'James', sep='**')

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Convert Decimal number to octal using print() output formatting.


input:


output:


hint:
Use the %o formatting code in print() function to format decimal number to octal.

Solution:
def oct_Decimal(num):
    print('%o'%num)

oct_Decimal(8)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Display float number with 2 decimal places using print().

input:
num = 458.541315

output:
res=458.54

Solution:
def disp_Fact_Val(val):
    print("%.2f" %val)
    print("%.4f" %val)

disp_Fact_Val(458.451315)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Accept a list of 5 float numbers as an input from the user.

input:
How many input value: -2
Enter float val: 10.12
Enter float val: 10.23

output:
res=[78.6, 78.6, 85.3, 1.2, 3.5]
res=[10.12, 10.23]

Hint:
-Create a list variable named numbers
-Run loop five times
-In each iteration of the loop, use the input() function to take input from a user
-Convert user input to float number using the float() constructor
-Add float number to the numbers list using the append() function

Solution:.
def input_float_val(term):
    output=[]
    for i in range(term):
        val=(float(input("Enter float val:")))
        output.append(val)
    print("Display input float values: ",output)

term=int(input("How many input value: "))
input_float_val(term)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Write all content of a given file into a new file by skipping line number 5

input:
test.txt file:
    line1
    line2
    line3
    line4
    line5
    line6
    line7

output:
line1
line2
line3
line4
line6
line7

Solution:
def readFile():
    with open("Code-1.py") as rf:
        contents=rf.read()

    print(contents)
readFile()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Write a program to take three names as input from a user in the single input() function call.

input:
name1, name2, name3 = input("Enter three string")

output:
Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly

Hint
Ask the user to enter three names separated by spaceSplit 
input string on whitespace using the split() function to get 
three individual names

Solution:
def input_Multiple_input():
    name1,name2,name3=input("Enter name: ").split()
    print(name1)
    print(name2)
    print(name3)

input_Multiple_input()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Write a program to use string.format() method to format the following 
three variables as per the expected output

input:
totalMoney = 1000
quantity = 3
price = 450

output:
I have 1000 dollars so I can buy 3 football for 450.00 dollars

Solution:
def formate_variable():
    name="kundan"
    phone=8072319818
    location="delhi"
    
    print("My name is {}, phone number {} and my current location is {}".format(name,phone,location))

formate_variable()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Write a program to check if the given file is empty or not

input:


output:

Hint
Use os.stat('file_name').st_size() function to get the file 
size. if it is 0 then the file is empty

Solution:
import os
def check_File_Empty_Not():
    size=os.stat("Code-9.py").st_size
    print("Empty" if (size==0) else"Not empty")
    
check_File_Empty_Not()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Read line number 4 from the following file.

input:
test.txt file:
line1
line2
line3
line4
line5
line6
line7

output:
line4

Solution:
def readLine():
    with open("Code-10.py") as r:
        #read all line from file
        lines=r.readlines()
        print(lines[6])
readLine()

#------------------------------------------------------------#











