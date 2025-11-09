# introToPython.py - Essential Python Concepts for Matrix Math

# --------------------------
# 1. Variables and Data Types
# --------------------------

# A variable is essentially a labeled container for a piece of data.
# In other programming languages like Java and C, we have to declare the type of our variables
# In python, we don't need to declare a type; Python figures it out.

# Integer (whole number)
rows = 2
# Floating-point number (number with a decimal)
scalar = 3.5
# String (text)
name = "Matrix A"
# Boolean (True or False)
is_square = False

# we can print things to the console like this:

print(rows) # output: 2
print(scalar) # output: 3.5

# --------------------------
# 2. Lists and Indexing
# --------------------------

# A list is an ordered, collection of items.
# It's what we use to represent rows and matrices in Python.

# Simple list (a row)
row_list = [10, 20, 30, 40]

# printing out the list:
print(row_list) # output: [10, 20, 30, 40]

# Indexing is how you access a specific element in a list.
# IMPORTANT: Indexing starts at 0, not 1!
# Indexing starts at 0 because it makes certain calculations easier in programming.

# Access the first element (index 0)
first_element = row_list[0] # This will be 10
# Access the third element (index 2)
third_element = row_list[2] # This will be 30
# Access the last element (index -1)
last_element = row_list[-1] # This will be 40

print(first_element) # output: 10
print(third_element) # output: 30
print(last_element) # output: 40

# Matrix is just a list of lists.
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_example) # output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# To access an element in a matrix, use two index pairs: [row_index][column_index]
# Element at Row 2 (index 1), Column 3 (index 2) -> the number 6
element_2_3 = matrix_example[1][2] 

print(element_2_3) # output: 6

# --------------------------
# 3. If/Else Statements
# --------------------------
# If/Else statements (or conditional statements) execute a block of code
# only if a specified condition is True.

number_of_rows = 3
number_of_cols = 3

# we use a double equals sign to check for equality
if number_of_rows == number_of_cols: # Check for equality
    print("This is a square matrix!")
# we can "attach" an else statement to this if statement, if we want code to be excecuted if the if statement is false

number_of_rows = 3
number_of_cols = 4

if number_of_rows == number_of_cols: # Check for equality
    print("This is a square matrix!")
else: 
    print("This is NOT a square matrix!")

# else statements cannot exist on their own, they must be related to an if statement

# Try changing number_of_rows or number_of_cols to see a different output!
# Other comparison operators: >, <, >=, <=, != (not equal)
# --------------------------
# 4. Functions
# --------------------------

# A function is a block of organized, reusable code that performs a single, related action.
# This helps keep your code organized and prevents repetition.

# Define a function using the 'def' keyword, followed by the function name and parameters in parentheses.
# the function's name "addTwoNumbers", can be anything, but it should be a short description of what the function does
# the "parameters" inside the paretheses are the values that will be used in the function
def addTwoNumbers(a, b):
    return a+b # this will return the sum of a and b
    # a return value is what the function's value will be after you "call" it

print(addTwoNumbers(1, 2)) # output: 3
# we can treat the function call of addTwoNumbers(1, 2) as the value 3, since the function returns the sum of 1 and 2
# this means we can use this to do whatever we want

print(addTwoNumbers(1, 2)+4) # output: 7