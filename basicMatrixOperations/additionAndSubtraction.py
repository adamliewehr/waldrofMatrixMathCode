# how can we add and subtract matricies in python? 

# well, as we know, adding and subtracting matricies is as simple as:
# adding or subtracting the elements in each matrix
# BUT, the matrices have to be of the same order
# lets create a function that checks whether two matricies are of the same order:

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8, 1],
           [10, 11, 1]]

# using what we know about python, we can create a function, that checks if two matrices are of the same order

def sameOrderCheck(matrix1, matrix2):
    # checks if the matrix has the same amount of rows, the collumns 
    if ((len(matrix1)==len(matrix2)) and (len(matrix1[0])==len(matrix2[0]))):
        return True
    else:
        return False
    
print(sameOrderCheck(matrix1, matrix2)) # output: True

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [10, 11]]

print(sameOrderCheck(matrix1, matrix2)) # output: False

# now that we have that function, we can create another function, called addMatricies

# this addMatricies takes two matrices
def addMatricies(matrix1, matrix2):
    if (sameOrderCheck(matrix1, matrix2)==False): # the two matrices are not of the same order
        print("Both matrices must be of the same order!")
        return False
    else:
        # TODO: ADD THIS IN
        pass