# List comprehensions provide a concise way to create lists.
# Syntax: [expression for item in iterable if condition]

# Example 1: Creating a list of cubes for numbers from 1 to 7.
cubes = [x ** 3 for x in range(1, 8)]
print(f"1. List of Cubes (1-7): {cubes}") 
# Output: [1, 8, 27, 64, 125, 216, 343]

# Example 2: Filtering names longer than 5 characters.
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frankie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(f"2. Filtered and Uppercased Names: {long_names}")
# Output: ['CHARLIE', 'FRANKIE']

# Example 3: Nested loops for creating a flat list of coordinates (x, y)
# Iterates through x = 1, 2 and y = 10, 20
coordinates = [(x, y) for x in [1, 2] for y in [10, 20]]
print(f"3. Nested List Comprehension (Coordinates): {coordinates}")
# Output: [(1, 10), (1, 20), (2, 10), (2, 20)]