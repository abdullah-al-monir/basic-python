# -----------------------------------------------------------------------------
# Description: Shows how to access and slice characters in a string.
# -----------------------------------------------------------------------------

my_string = "Programming"

# Accessing characters using positive indexing (from the left, starting at 0)
print(f"First character: {my_string[0]}")      # Output: P
print(f"Fifth character: {my_string[4]}")      # Output: a

# Accessing characters using negative indexing (from the right, starting at -1)
print(f"Last character: {my_string[-1]}")      # Output: g
print(f"Third from end: {my_string[-3]}")      # Output: i

# Slicing a substring from a string
# Syntax: [start:end] (end index is exclusive)
print(f"Slice from index 2 to 6: {my_string[2:7]}")  # Output: ogram
print(f"Slice from start to index 4: {my_string[:5]}")  # Output: Progr
print(f"Slice from index 3 to end: {my_string[3:]}")   # Output: gramming

# Reversing a string using slicing
print(f"Reversed string: {my_string[::-1]}")  # Output: gnimmargorP
