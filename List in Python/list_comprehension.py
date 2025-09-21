# -----------------------------------------------------------------------------
# Description: Demonstrates using list comprehension for concise list creation.
# -----------------------------------------------------------------------------

# Traditional way to create a list of squares
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(f"Squares using a loop: {squares}")

# The same task using list comprehension (more concise)
# Syntax: [expression for item in iterable if condition]
comprehension_squares = [i**2 for i in range(1, 6)]
print(f"Squares using list comprehension: {comprehension_squares}")

# Using a list comprehension with a condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers from 0 to 9: {even_numbers}")

# A comprehension with multiple loops (for nested lists)
nested_list = [(x, y) for x in range(2) for y in range(3)]
print(f"Nested loops comprehension: {nested_list}")

