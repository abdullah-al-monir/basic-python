# -----------------------------------------------------------------------------
# Description: Shows how to loop through a list and work with nested lists.
# -----------------------------------------------------------------------------

# Iterating over a list using a for loop
print("Iterating through fruits:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n--- Working with Nested Lists ---")

# A nested list representing a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(f"The element at row 1, column 2 is: {matrix[1][2]}")
print(f"The last element of the last row is: {matrix[-1][-1]}")
