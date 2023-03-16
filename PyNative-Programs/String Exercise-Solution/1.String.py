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
Write a program to create a new string made of an input string’s first, middle, and last character.

input:
str1 = "James"

output:
res=Jms

Solution:
def firstMiddleLastChar(str1):
    print(str1[0]+str1[((len(str1))//2)]+str1[-1])
str1="James"
firstMiddleLastChar(str1)

#------------------------------------------------------------#



#------------------------------------------------------------#
Question-1.2:
Write a program to create a new string made of the middle three characters of an input string.

input:
str1 = "JhonDipPeta"
str2 = "JaSonAy"

output:
res=Dip
res1=Son

Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-2:
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

input:
s1 = "Ault"
s2 = "Kelly"

output:
AuKellylt

Solution:
def insertWordMiddle(s1,s2):
    l=(len(s1))//2
    output=s1[:l:]+s2+s1[l::]
    print(output)


s1="ABCDEFGH"
s2="Kelly"
insertWordMiddle(s1,s2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

input:
s1 = "America"
s2 = "Japan"

output:
AJrpan

Solution:
def firstMiddleLast(s1,s2):
    s3=""
    l1=(len(s1))//2
    l2=(len(s2))//2
    s3=s1[0]+s2[0]+s1[l1]+s2[l2]+s1[-1]+s2[-1]
    print(s3)

#s1 = "America"
#s2 = "Japan"

s1="ABCDE"
s2="abcde"
firstMiddleLast(s1,s2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

input:
str1 = PyNaTive

output:
yaivePNT

Solution:
def sortChar(s1):
    lower=""
    upper=""
    for ch in s1:
        if ch.islower():
            lower=lower+ch
        else:
            upper=upper+ch 
    print(lower+upper)


s1="ABCDabcdefAfd"
sortChar(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Count all letters, digits, and special symbols from a given string

input:
str1 = "P@#yn26at^&i5ve"

output:
Total counts of chars, digits, and symbols 
Chars = 8 
Digits = 3 
Symbol = 4

Solution:
def findLetterDigitsSpecilSymbol(s1):
    ch,dig,sp=0,0,0
    for c in s1:
        if c.isalpha():
            ch=ch+1
        elif c.isdigit():
            dig=dig+1
        else:
            sp=sp+1
    print("Total length of string: ",len(s1))
    print("Number of character: ",ch)
    print("Number of digit: ",dig)
    print("Number of specil char: ",sp)

s1 = "P@#yn26at^&i5ve"
findLetterDigitsSpecilSymbol(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Given two strings, s1 and s2. Write a program to create a new string s3 
made of the first char of s1, then the last char of s2, Next, the second 
char of s1 and second last char of s2, and so on. Any leftover chars go at 
the end of the result.

input:
s1 = "Abc"
s2 = "Xyz"

output:
AzbycX

Solution:
def mixedString(s1,s2):
    val=""
    l=len(s1)
    for i in range(len(s1)):
        val=val+s1[i]+s2[i-l]
    print(val)


s1="ABCD"
s2="abcd"
mixedString(s1,s2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Write a program to check if two strings are balanced. For example, 
strings s1 and s2 are balanced if all the characters in the s1 are 
present in s2. The character’s position doesn’t matter.

input:
Case 1:
s1 = "Yn"
s2 = "PYnative"

Case 2:
s1 = "Ynf"
s2 = "PYnative"

output:
True
False

Solution:
def balanceString(s1,s2):
    c=0
    for ch in s2:
        if ch in s1:
            c=c+1
        else:
            break
    print("balance" if (c==(len(s2))) else "Not balance")

s1="Python"
balanceString(s1,"on")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Write a program to find all occurrences of “USA” in a given string ignoring the case.

input:
str1 = "Welcome to USA. usa awesome, isn't it?"

output:
The USA count is: 2

Solution:
def occurrenceSubString(str1,sub_str):
    s1=str1.upper()
    s2=sub_str.upper()
    print("The",s2,"count is: ",s1.count(s2)) 
   
    
str1="Welcome to USA. usa awesome, isn't it?"
sub_str="usa"
occurrenceSubString(str1,sub_str)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Given a string s1, write a program to return the sum and average of the 
digits that appear in the string, ignoring all other characters.

input:
str1 = "PYnative29@#8496"

output:
Sum is: 38 Average is  6.333333333333333

Solution:
def sumAverage(s1):
    sum,ch,c=0,0,0
    for ch in s1:
        if ch.isdigit():
            sum=sum+int(ch)
            c=c+1
    print("sum of number: ",sum)
    print("Average:",(sum/c))

s1="PYnative29@#8496"
sumAverage(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Write a program to count occurrences of all characters within a string.

input:
str1 = "Apple"

output:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}

Solution:
def countOccurrence(s1):
    dic={}
    for ch in s1:
        dic[ch]=dic.get(ch,0)+1
    print(dic)


s1="countoccurrence"
countOccurrence(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-11:
Reverse a given string

input:
str1 = "PYnative"

output:
evitanYP

Solution:
def reverseString(s1):
    print(s1[::-1])

s1="python code"
reverseString(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-12:
Write a program to find the last position of a substring “Emma” in a given string.

input:
str1 = "Emma is a data scientist who knows Python. Emma works at google."

output:
Last occurrence of Emma starts at index 43

Solution:
def findLastPosition(s1,sub_str):
    print("Last occurentce of",sub_str,"starts at index:",s1.rfind(sub_str))


s1="Emma is a data scientist who knows Python. Emma works at google."
sub_str="Emma"
findLastPosition(s1,sub_str)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-13:
Write a program to split a given string on hyphens and display each substring.

input:
str1 = Emma-is-a-data-scientist

output:
Displaying each substring

Emma
is
a
data
scientist

Solution:
def spliteString(s1):
    lst=s1.split("-")
    for val in lst:
        print(val)

s1 = "Emma-is-a-data-scientist"
spliteString(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-14:
Remove empty strings from a list of strings

input:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

output:
Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

Solution:
def removeEmptyString(lst):
    output=[]
    print("Original list of sting\n",lst)
    for val in lst:
        if val=="":
            continue
        else:
            output.append(val)

    print("\nAfter removing empty strings\n",output)


lst=['Emma', 'Jon', '', 'Kelly', None, 

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-15:
Remove special symbols / punctuation from a string

input:
str1 = "/*Jon is @developer & musician"

output:
"Jon is developer musician"

Solution:
def removeSpecialSymbols(s1):
    output=""
    for ch in s1:
        if ch.isdigit() or ch.isalpha() or ch==" ":
             output=output+ch
           
    print(output)


s1="/*Jon is @developer & musician"
removeSpecialSymbols(s1)

#------------------------------------------------------------#

#------------------------------------------------------------#
Question-16:
Removal all characters from a string except integers

input:
str1 = 'I am 25 years and 10 months old'

output:
2510

Solution:
def removeAllCharacterExceptString(s1):
    for ch in s1:
        if ch.isdigit():
            print(ch,end="")

s1='I am 25 years and 10 months old'
removeAllCharacterExceptString(s1)

#---------------------------------------------------------


#------------------------------------------------------------#
Question-17(NT):
Write a program to find words with both alphabets and numbers from an input string

input:
str1 = "Emma25 is Data scientist50 and AI Expert"

output:
Emma25
scientist50

Solution:


#---------------------------------------------------------


#------------------------------------------------------------#
Question-18:
Replace each special symbol with # in the following string

input:
str1 = '/*Jon is @developer & musician!!'

output:
##Jon is #developer # musician##

Solution:
def replaceHash(s1):
    op=""
    for ch in s1:
        if ch.isdigit() or ch.isalpha() or ch==" ":
            op=op+ch
        else:
            op=op+"#"
    print(op)

    

s1='/*Jon is @developer & musician!!'
replaceHash(s1)

#---------------------------------------------------------








