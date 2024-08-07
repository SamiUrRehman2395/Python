# ******************************************************************************
# 1. printing first programme
print("Hello World")



# ******************************************************************************
# 2. Variables
name = "Sami Ur Rehman"
age = 19
cgpa = 3.5
is_programmer = True

print(name)
print(age)
print(cgpa)
print(is_programmer)



# ******************************************************************************
# 3. Taking input
myName = input("\nWhat's your name? ")
print("Hello ! My name is " + myName) #concatenation



# ******************************************************************************
# 4. Type conversion
old_age = input("\nWhat was you age till 2022? ")
age_now = int(old_age) + 2 #all inputs python consider string, so we convert it into integer this way
print("Now my age is", age_now)



# ******************************************************************************
# 5. Sum of two numbers
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
sum = int(num1) + int(num2) #it will add these two numbers and give 5 as output
sum2 = num1 + num2 # it will concatenate and give 23 as output if we enter 2 and 3
print("the sum is", sum)
print(sum2)



# ******************************************************************************
# 6. String

# 6.1 - upper and lower case
name1 = "Sami Ur Rehman"
print(name.upper())
print(name.lower())

# 6.2 - finding character
print("This character is at index", name1.find('R'))

# 6.3 - replacing chracter or String
print(name1.replace("Sami Ur Rehman", "Sami-ur-Rehman"))
print(name1) #it will not change the original string by the way , so if we print name1 again , iw will give originl string

# 6.4 - to find if the character or string or substring exists or not
burger = "Smashed Beef Burger"
print("Smashed" in burger) #it will give true or false as output



# ******************************************************************************
# 7. Arithmetic Operators

print (5+2) # output = 7
print (5-2) # output = 3
print (5*2) # output = 10
print (5/2) # output = 2.5
print (5//2) # output = 2 (floor division gives value before decimal point)
print (5%2) # output = 1 (modulo gives remainder)

# 7.1 - Shortcuts
i = 5
i = i + 2

#we can write this in this way 
i += 2



# ******************************************************************************
# 8. Comparision Operators
'''
> (greater than)
< (less than)
>= (greater than equals to)
<= (less than equals to)
== (equal to equal to)
!= (not equal to)

'''
#examples
print(2<3) #output = true
print(2>3) #output = false



# ******************************************************************************
# 9. Logical Operators
'''
And (return true if all the conditions are true)
OR (return true if any one of the conditions are true)
NOT (make true, false ; and ; false, true)

'''
#examples
print(4 > 3 or 2 > 3) #one condition is true, output will be true
print(4 > 3 and 2 > 3) #one condition is true, output will be false
print(not 4>3) #4 is greater than 3 , but it will return false as output



# ******************************************************************************
# 10. Conditional Statements

# 10.1 - IF , Else-If , Else
myAge = 19
if age >=18:
    print("Is an Adult")
    print("Can cast Vote")
elif age <18:
    print("Not an Adult")   
    print("Cannot cast Vote")
else:
    print("Invalid input")   
  
  
    
# ******************************************************************************
# 11. Range
range(5) # mean 0 to 5 ... 0, 1, 2, 3, 4



# ******************************************************************************
# 12. Loops

# 12.1 - While Loop
i = 1
while i <=100:
    print(i)    
    i = i+1
    
#it will print 1 to 100

while i <=5:
    print(i * "*")
    
#it will print this pattern
'''

*
**
***
****
*****

'''    

# 12.2 - For Loop
for i in range(5):
    print(i)
#it will print 0 to 4
    print(i + 1)
#it will print 1 to 5



# ******************************************************************************
# 13. List    
marks = [75, 71, 87, 75, 61]
print(marks)

#we can also store different type of data types
marks1 = [1, "ABC"]
print(marks1)

#if we need only 1 specific number, we can print from its index number
marks = [75, 71, 87, 75, 61]
print(marks[0]) # output : 75

#another variation
print(marks[-1]) # output : 61 ; -1 means start from last
#if we write -2, it will print 75 , second last

#if we wanna get some numbers , not all
print(marks[0:2])
#it will print 0th and 1st index and not 2nd, 0 will include but 2 will not


#another way to print ; with for loop
for score in marks:
    print(score) #it will print all the numbers that are stored in marks
    
# 13.1 - Other operations we can do in list

# 13.1.1 - Append
marks.append(100)   # it will add 100 to that list
print(marks)

# 13.1.2 - Insert
marks.insert(1, 50) # it will insert 50 at 1st index
print(marks)

# 13.1.3 - Length
print(len(marks)) # it will give size of list
    
#we can print list with while loop, this way
i = 0
while i < len(marks):
    print(marks[i])
    i = i+1    

# 13.1.4 - Clear

marks.clear()
print(marks) #it will clear the list



# ******************************************************************************
# 14. Break and Continue

Cricketers = ["Fakhar", "Babar", "Imad", "Amir", "Naseem"]
#if we want to print names till Imad
for i in Cricketers:
    if i == "Imad":
        break
    print(i)
    
#if we want to print names except Babar
for j in Cricketers:
    if j == "Babar":
        continue
    print(i) 
#babar will be skipped  
    
    
    
# ******************************************************************************
# 15. Tuple

numbers = (95, 98, 97, 97, 97)
#tuple is immutale; cant be changed

print(numbers.index(98)) # output : 1
print(numbers.index(97)) # output : 2 ; give index at which repeated number comes first
print(numbers.count(97)) # output : 3 ; counts how many time 97 comes in this tuple



# ******************************************************************************
# 16. Sets

scores = {210, 193, 174, 174}
print(scores) # output : {210, 193, 174} ; gives unique elements, and not repeative

#can"t acces by index like this : print(marks[1])

#can access with the help of loops
for a in scores:
    print(a)
    
# sets are un-ordered ; can give elements at any position
# for example, it can print like this : 174, 210, 193



# ******************************************************************************
# 17. Dictionary

# key : value ; to store values in pairs

playersShirtNo = {"Guptill" : 31 , "Virat" : 18 , "DeVilliers" : 17}

print(playersShirtNo["Guptill"])

#if we wanna add a player

playersShirtNo["Shan Masood"] = 94;
print(playersShirtNo) # it will give all 4 in output including Shan Masood



# ******************************************************************************
# 18. Functions

# 18.1 - In-Built Functions
'''
int()
str()
bool()  

etc
'''


# 18.2 - Module Functions

import math
print(dir(math))
#it will print all the functions present in math

from math import sqrt
# sqrt is a square root function from math
print(sqrt(16)) # output : 4.0

from math import *
# it will import all functions from math


# 18.3 - User-Defined Functions

#function definition
def print_sum(number1, number2):
    print(number1 + number2)
    
#function call
print_sum(2, 2) # output : 4

