# If we want to generate a matrix in python, it is fairly easy
# we just use lists

# What is a list?

# A list is a a collection of items (strings, integers, floating point numbers, anything!)
# for our case, we will just use integers

# Simple list:

list1 = [1, 2, 3]

# We can print this out using print()

print("This is a list:")
print(list1) # output: "[1, 2, 3]"
# try changing list1 and see what happens!

# since we can put prety much anything in a list, we can also put another list, inside a list
# a matrix is just a list with more lists inside of it
# like this:

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("This is a matrix:")
print(matrix1)
# try changing matrix1 to see what happens!


# both the matrix in our code, and the output doesn't really look like a matrix though
# we can format out code easily using the enter key
# this creates a new line in our code, which makes it easier to read

matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

# But our output will still be the same

print(matrix1)

# How can we output a matrix so it actually looks like a matrix?
# Well, there are several ways to do this (good and bad)
# lets start with the bad

print(matrix1[0])
print(matrix1[1])
print(matrix1[2])

# this is what we call "indexing" in programming. We use the [] brackets with a number inside
# to indicate what element we want to retreive

# that looks like what we want, but this is what is called hard coding, which is the "bad" way
# hard coding is when we write our program in a way where the program's behavior is tied to a specific input
# this may work for the matrix we have now, but lets try the same thing for another matrix

matrix1 = [[1, 2,  3,  4], 
           [5, 6,  7,  8], 
           [9, 10, 11, 12], 
           [13, 14, 15, 16]]

# now if we try to print it using the same exact code:

print(matrix1[0])
print(matrix1[1])
print(matrix1[2])

# our output is not printing out our complete matrix!
# becuase we hard coded our first matrix which was a 3x3 matrix, our output code doesn't work for a 4x4 matrix
# for matrices of variable sizes, we need to write a program that can print out the matrix, no matter what the order is
# for this, we use something called a for loop!

# A for loop is a loop (who could have guessed!) that is used for iterating over a sequence (such as a list)
#  It allows you to execute a block of code repeatedly, once for each item in the sequence. 

# So, to print out a matrix, no matter the size, we can write this program:

def printMatrix(matrix):
    for row in matrix:
        print(row)

# Now we can give it the previous matrix:

print("Printing the full matrix:")
printMatrix(matrix1)
# try changing matrix 1 to see what happens!
# as we can see, this prints out the full matrix, no matter what the order is!
# this is because the for loop goes through each row in the matrix, and prints it out
# this is a much better way to print out a matrix!
