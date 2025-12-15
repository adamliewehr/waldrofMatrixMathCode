
# order: 4x3
matrix1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [4, 6, 7]
]

# rows:
print(len(matrix1))
# cols
print(len(matrix1[0]))

# print out the following values:
# row 3, col 2
print(matrix1[2][1])
# row 4, col 3
print(matrix1[3][2])
# row 1, col 2
print(matrix1[0][1])

# looping through the matrix:
# for row in matrix1:
#   print(row)
#   for number in row:
#     print(number)

for rowIndex in range(len(matrix1)):
  print(matrix1[rowIndex])
  for colIndex in range(len(matrix1[0])): # assuming the matrix is valid
    print(matrix1[rowIndex][colIndex])

# class activity
# adding the "mirrored" element in each list 
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# desired output: [7, 9, 11, 13, 15]

answer = []
for index in range(len(list1)):
  answer.append(list1[index] + list2[index])

print(answer)

# intro to modulo and floor division

# floor division (integer division) -> //
print(17 // 5) # 3  -> whole number quotient
print(130 // 60) # 2  -> full hours in 130 minutes

# modulo (remainder)
print(17 % 5) # 2  -> remainder
print(23 % 4) # 3  -> leftover when making groups of 4


