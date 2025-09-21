# -----------------------------------------------------------------------------
# Description: Shows how to access and modify list elements using indexing.
# -----------------------------------------------------------------------------

my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing elements using positive indexing
print(f"First element: {my_list[0]}")
print(f"Fourth element: {my_list[3]}")

# Accessing elements using negative indexing
print(f"Last element: {my_list[-1]}")
print(f"Second to last: {my_list[-2]}")

# Slicing a portion of the list
# Syntax: [start:end] (end is exclusive)
print(f"Slice from index 1 to 3: {my_list[1:4]}")
print(f"Slice from the start to index 2: {my_list[:3]}")
print(f"Slice from index 2 to the end: {my_list[2:]}")

# Modifying an element at a specific index
my_list[1] = "blackberry"
print(f"Modified list: {my_list}")
