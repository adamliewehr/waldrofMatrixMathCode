# matrix multiplication is a bit more complex than addition and subtraction
# to multiply two matrices, the number of columns in the first matrix must equal the number of rows in the second matrix
# for example, if matrix A is of size 2x3 (2 rows, 3 columns) and matrix B is of size 3x4 (3 rows, 4 columns),
# then we can multiply A and B to get a new matrix C of size 2x4 (2 rows, 4 columns)



# we need to check if the the number of columns in the first matrix must equal the number of rows in the second matrix
# we can use the getMatrixOrder function from matrixIntro/basicConcepts.py to do this
# lets just copy it over here for simplicity

def getMatrixOrder(matrix):
    return (len(matrix), len(matrix[0]))

# now we can create a function that checks if two matrices can be multiplied

def canMultiply(matrix1, matrix2):
    order1 = getMatrixOrder(matrix1)
    order2 = getMatrixOrder(matrix2)
    if order1[1] == order2[0]: # number of columns in matrix1 == number of rows in matrix2
        return True
    else:
        return False
    
A = [[2, 4, 6]] # 1x3
B = [[3],
     [6],
     [9]] # 3x1
C = [[1, 2, 3], 
     [4, 5, 6]] # 2x3
D = [[7, 8],
     [9, 10],
     [11, 12]] # 3x2
    
print(canMultiply(A, B)) # output: True
print(canMultiply(B, C)) # output: False
print(canMultiply(C, D)) # output: True

def multiplyMatrices(matrix1, matrix2):

    if (canMultiply(matrix1, matrix2)): # if the matrices are compatible for multiplication
        result = [] # create the matrix that will store the number we get from the multiplcation
        
        for matrix1Row in range(len(matrix1)):

            currentRow = matrix1[matrix1Row]

            for i in range(len(matrix2[0])):
                currentCol = []
                for j in range(len(matrix2)):
                    currentCol.append(matrix2[j][i])
                
                # print("currentRow:", currentRow)
                # print("currentCol:", currentCol)
                # print("")

                sum = 0
                for k in range(len(matrix1[matrix1Row])):
                    sum+=currentRow[k]*currentCol[k]

                result.append(sum)

        # now that we have the values of the result matrix in a list
        # we can populate the finalResult matrix one by one
        # there is def a better way to do this
        # but my brain was feeling small at the moment I was programming this



        for rowNum in range(getMatrixOrder(matrix1)[0]):
            temp = []
            for colNum in range(getMatrixOrder(matrix2)[1]):
                temp.append(result.pop(0))

            result.append(temp)


        return result # return the result matrix
    
    else:
        return False
    
# if we multiple matrix A (1x3) and B (3x1), we should get a 1x1 matrix
    
print("CD")
print(multiplyMatrices(C, D))

print("AB")
print(multiplyMatrices(A, B))

