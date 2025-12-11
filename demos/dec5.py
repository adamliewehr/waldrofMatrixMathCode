# continuing conditional statements

age = 18

# we can also use and/or statements to combine multiple conditions
if age >= 18 and age < 21:
    print('you can vote but not drink')

if age < 18 or age >= 65:
    print('you get a discount!')

# nested if statements
if age >= 18:
    if age >= 21:
        print('you can drink')
    else:
        print('you cannot drink yet')

# that's it for if/else statements!

# lists
# a list is an ordered collection of items

my_list = [5, 10, 15, 20, 25]

print(my_list)  # prints the entire list

# we can access individual items in a list using indexing
# indexing starts at 0
# this is because it makes certain calculations easier in programming
first_item = my_list[0]
second_item = my_list[1]
last_item = my_list[-1]  # negative indexing starts from the end

print("First item:", first_item)
print("Second item:", second_item)
print("Last item:", last_item)

# we can also have lists of lists, which is how we represent matrices
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:", matrix)

# accessing elements in a matrix
element_2_3 = matrix[1][2]  # Row 2, Column 3 (remember indexing starts at 0)
print("Element at Row 2, Column 3:", element_2_3)

# loops

# loops let us repeat code multiple times

for i in range(5):  # this will run the code inside the loop 5 times
    print("This is loop iteration number:", i)

# i is a variable that changes each time the loop runs
# it starts at 0 and goes up to (but does not include) 5

# we can use loops to go through lists

for item in my_list:
    print("List item:", item)

