# Finding the order of a matrix

# To find the order of a matrix, we need to know the number of rows, and the number of columns

matrix1 = [[1, 2,  3,  4], 
           [5, 6,  7,  8], 
           [9, 10, 11, 12]]

# just by looking at this matrix, we can see that it is a 3x4 matrix
# but how do we output that in code?
# we can use the len() function
# functions are things we can use to get certain information from specific data
# the len function returns the length of the list we put into it
# for example

print(len([1, 2, 3])) # output: 3
# try changing the length of this list, and see what happens!

# to print out the order of a matrix, it is more simple than you'd think
# since all matrices are rectangles, and all rows have the same amount of values,
# we can simply get the length of the entire matrix, and the length of the first row
# so, using matrix1

print("The order of this matrix is: ", len(matrix1), "x", len(matrix1[0])) # output: "The order of this matrix is:  3 x 4"
# try changing the length of the rows and columns of matrix1 and see what happens!

# to get a specific element in a matrix, it is very similar to what we would do on paper
# except there is one catch: indexing in programming starts at 0 not 1
# what does this mean? 
# well, before when we wanted to specify a certain element in a matrix we would do something like this:
# matrix1(2, 3) = 7
# we are saying that the number 7 is in row 2 and column 3
# but in python, we don't start at 1, we start at 0
# So, to access the element that contains the number 7, we would write this:

print(matrix1[1][2]) # output: 7
# try changing the numbers in this line, and see what happens!

# Square matrices are matrices where the rows and columns are of the same degree
# how could we write a program to see if a matrix is a square matrix?

# we could use something called an "if statement"
# if statements are used for conditional execution, allowing a block of code to run only if a specified condition evaluates to True.

# for example:

if (1 < 2): # english translation: "if 1 is less than 2, print 'True!'"
    print('True!')
    # try changing the numbers and sign to see what happens!

# we can use this to check if the degree of the rows and columsn are the same

def squareMatrixCheck(matrix):
    if (len(matrix) == len(matrix[0])):
        print("This is a square matrix!")
    else: 
        print("This is not a square matrix.")

squareMatrixCheck(matrix1) # output: "This is not a square matrix."

# lets try with a square matrix

matrix2 = [[1, 2],
           [3, 4]]

squareMatrixCheck(matrix2) # output: "This is a square matrix!"