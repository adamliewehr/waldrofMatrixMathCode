# your first program!
print("Hello world!")
# printing is usueful in many ways

# Comments are a way to document your code!

# Variables:
# variables are just labeled boxes you can store stuff in
name = 'Adam'
age = 21
height_meters = 1.8034
tired = True

# we can print these out the same way we print out anything else
print(name)

# values have different types
# 1. Integers (int): Whole numbers, e.g., 1, -5, 100
# 2. Floating-point numbers (float): Numbers with decimal points, e.g., 3.14, -0.001
# 3. Strings (str): Text enclosed in quotes, e.g., "Hello, World!"
# 4. Booleans (bool): True or False values

# we can check these types using the type() function

print(type(name)) # output: <class 'str'>

# input function:
# we can get input from the user by using the input() function

userName = input("please enter your name: ")
# now if we print out userName, we will see whatever we entered
print(userName)

# we can "add" strings together to form a longer string, this is called concatenation
# like this:
print("my name is " + userName)

# lets try to get more input from the user
userAge = input("please enter your age: ")
print(userAge)

# lets try to add one year to my age
# print(userAge+1) # i commented this out so we wouldn't get an error

# we got an error!
# errors tell us what we did wrong, we just have to learn how to read them
# File "/Files/main.py", line 43, in <module>
#     print(userAge+1)
#           ~~~~~~~^~
# TypeError: can only concatenate str (not "int") to str

# this is what the console outputs

# it says we cannot concatentae a string and another object, why did we get this error?
# the input() function "returns" a string, and since we tried to add 1 to the string "21", we got an error
# this means that even though we entered a number, a string is stored in the userAge variable
# if we entered 21, "21" (notice the quotes) is stored in the variable
# how do we convert our userAge to an int?

# each type has its own function: int(), str(), float(), bool()
# this lets us convert valid values into the type of our choice
# this allows us to use it correctly

# we can also use commas, instead of adding two strings together
print("This is your age in 67 years:", int(userAge)+67)
# if we did add (or concatenate) the two strings together, we would have to convert the result back to a string
# like this:
print("This is your age in 67 years: " + str(int(userAge)+67))

# if statments let us run code conditionally
# this means that code under an if statement only runs if the statement after the if statement is true.
# like this:

age = 21

if age > 18:
    print('unc')

# we can have multiple if statements in a program

if age >= 21:
    print('have a drink!')

if age < 18:
    print('child')

# else statements let us run code when the if statement is false
if age < 18:
    print('child')
else:
    print('adult')

# else statements can only come after an if statement
# we can also use elif statements to check multiple conditions
if age < 13:
    print('child')
elif age < 18:
    print('teen')
else:
    print('adult')


