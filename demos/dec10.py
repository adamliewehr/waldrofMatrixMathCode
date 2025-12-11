
# 1. While loop

print("While loop demo:")
count = 0                 # start value
while count < 5:          # loop as long as this condition is True
    print("count is:", count)
    count = count + 1            # update so we eventually break out of the loop

# example 2

total = 0

user_input = input("Enter a number (or 'quit' to stop): ")

# Keep looping while the user does NOT type 'quit'
while user_input != "quit":
    # Convert the input string to an integer and add it to the total
    number = int(user_input)
    total = total + number
    print("Current total:", total)

    # Ask again at the end of the loop
    user_input = input("Enter a number (or 'quit' to stop): ")

print("Final total is:", total)

# 2. Matrices as lists of lists

# A matrix is often represented in Python as a list of rows.
# Each row is itself a list.
matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]

print("Matrix representation (list of lists):")
print(matrix)    # prints the whole matrix structure

# getting the order of a matrix using the len() function
# rows:
print(len(matrix))
# cols
print(len(matrix[0]))

# 3. Indexing into a matrix

# General pattern: matrix[row_index][column_index]

print("Indexing into matrix:")
print("Top-left element (row 0, col 0):", matrix[0][0])  # 1
print("Middle element  (row 1, col 1):", matrix[1][1])   # 5
print("Bottom-right element (row 2, col 2):", matrix[2][2])  # 9

# 4. Nested for loops over a matrix

print("Nested for-loop over all elements:")
for row in matrix:
    print(row)
    for number in row:    
        print(number)

