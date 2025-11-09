# how can we add and subtract matricies in python? 

# well, as we know, adding and subtracting matricies is as simple as:
# adding or subtracting the elements in each matrix
# BUT, the matrices have to be of the same order
# lets create a function that checks whether two matricies are of the same order:

# wait a second, we have a function in matrixIntro/basicConcepts.py that gets the order of a matrix
# we can use that to check if two matrices are of the same order

# let's quickly rewrite that function here

def getMatrixOrder(matrix):
    return (len(matrix), len(matrix[0]))

# now we can use that function to check if two matrices are of the same order

# example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8, 1],
           [10, 11, 1]]

# using what we know about python, we can create a function, that checks if two matrices are of the same order
# we can use the imported getMatrixOrder function here

def sameOrderCheck(matrix1, matrix2):
    # checks if the matrix has the same amount of rows, the collumns 
    if getMatrixOrder(matrix1) == getMatrixOrder(matrix2):
        return True
        # we just used a function inside another function!
    else:
        return False
    
print(sameOrderCheck(matrix1, matrix2)) # output: True

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [10, 11]]

print(sameOrderCheck(matrix1, matrix2)) # output: False

# now that we have that function, we can create another function, called addMatricies
# this function will add two matrices
# it will return a new matrix that is the sum of the two input matrices
# the resulting matrix will have the same dimensions as the input matrices

# this addMatricies takes two matrices
def addMatricies(matrix1, matrix2):
    if (sameOrderCheck(matrix1, matrix2)==False): # the two matrices are not of the same order
        print("Both matrices must be of the same order!")
        return False
    else:
        result = [] # create an empty list to store the result matrix
        # loop through each row
        for row in range(len(matrix1)):
            resultRow = [] # create an empty list to store the current row of the result matrix
            # loop through each column
            for col in range(len(matrix1[0])):
                # add the corresponding elements from both matrices
                resultRow.append(matrix1[row][col] + matrix2[row][col])
            result.append(resultRow) # add the current row to the result matrix
        return result
    
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8, 9],
           [10, 11, 12]]

print(addMatricies(matrix1, matrix2)) # output: [[8, 10, 12], [14, 16, 18]]
# now that we have addMatricies, we can create subtractMatricies in a similar way

# this is basically the exact same as addMatricies, but instead of adding, we subtract
def subtractMatricies(matrix1, matrix2):
    if (sameOrderCheck(matrix1, matrix2)==False): # the two matrices are not of the same order
        print("Both matrices must be of the same order!")
        return False
    else:
        result = [] # create an empty list to store the result matrix
        # loop through each row
        for row in range(len(matrix1)):
            resultRow = [] # create an empty list to store the current row of the result matrix
            # loop through each column
            for col in range(len(matrix1[0])):
                # subtract the corresponding elements from both matrices
                resultRow.append(matrix1[row][col] - matrix2[row][col])
            result.append(resultRow) # add the current row to the result matrix
        return result
    
matrix1 = [[10, 20, 30],
           [40, 50, 60]]

matrix2 = [[1, 2, 3],
           [4, 5, 6]]

print(subtractMatricies(matrix1, matrix2)) # output: [[9, 18, 27], [36, 45, 54]]

