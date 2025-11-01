# scalar multiplication is when we multiply a matrix by a scalar (a single number)
# to do this, we simply multiply each element in the matrix by the scalar
# this is similar to addition and subtraction of matrices, but instead of adding or subtracting the elements, we multiply them

def scalarMultiplication(matrix, scalar):
    result = [] # create an empty list to store the result matrix
    # loop through each row
    for row in range(len(matrix)):
        resultRow = [] # create an empty list to store the current row of the result matrix
        # loop through each column
        for col in range(len(matrix[0])):
            # multiply the current element by the scalar
            resultRow.append(matrix[row][col] * scalar)
        result.append(resultRow) # add the current row to the result matrix
    return result

matrix = [[1, 2, 3],
          [4, 5, 6]]

scalar = 2
result = scalarMultiplication(matrix, scalar)
print(result) # output: [[2, 4, 6], [8, 10, 12]]

scalar = 0.5
result = scalarMultiplication(matrix, scalar)
print(result) # output: [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

scalar = -1
result = scalarMultiplication(matrix, scalar)
print(result) # output: [[-1, -2, -3], [-4, -5, -6]]

# as we can see, scalar multiplication is a simple operation that involves multiplying each element in the matrix by the scalar
# this can be useful in various applications, such as scaling matrices or transforming data
# we can also use scalar multiplication in combination with addition and subtraction of matrices
# for example, we can scale a matrix and then add it to another matrix

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8, 9],
           [10, 11, 12]]

from additionAndSubtraction import addMatricies # importing the addMatricies function from additionAndSubtraction.py
# importing a function from another file is done using the "from [filename] import [functionname]" syntax

scaledMatrix1 = scalarMultiplication(matrix1, 2) # scale matrix1 by 2
result = addMatricies(scaledMatrix1, matrix2) # add the scaled matrix to matrix2
print(result) # output: [[9, 12, 15], [18, 21, 24]]