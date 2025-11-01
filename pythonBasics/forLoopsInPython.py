
# for loops are a foundational concept in programming
# they let us loop through arrays, and produce long lists of numbers with ease
# the basic for loop structure is this:

sampleList = [1, 2, 3, 4, 5]

for i in sampleList:
    print(i)

# output:
# 1
# 2
# 3
# 4
# 5

# what this does, is it loops through each value in sampleList and prints it out
# but how?
# the "for i in" part means "for each element in the array, assign it to the variable i"
# then, the code indented under the for loop is executed for each value of i
# so, in this case, it prints out each value in sampleList

# we can also use for loops to create lists of numbers
numberList = []

for i in range(1, 11): # range(1, 11) creates a list of numbers from 1 to 10
    numberList.append(i) # append adds the value of i to the end of numberList

print(numberList) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we can also use for loops to loop through multi-dimensional arrays (like matrices)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    for col in row:
        print(col)

# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# in this example, we have a nested for loop
# the outer loop loops through each row in the matrix
# the inner loop loops through each column in the current row
# and prints out each value

# we can also use range() and len() to loop through the indices of a matrix

for row in range(len(matrix)): # loop through the row indices
    for col in range(len(matrix[0])): # loop through the column indices
        print(matrix[row][col])

# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# in this example, we use len(matrix) to get the number of rows
# and len(matrix[0]) to get the number of columns
# then, we use those values to loop through the indices of the matrix
# and print out each value using matrix[row][col]

# for loops are a powerful tool in python, and are essential for working with arrays and matrices
# now that we have a basic understanding of for loops, we can use them to implement matrix addition and subtraction
# as seen in basicMatrixOperations/additionAndSubtraction.py

