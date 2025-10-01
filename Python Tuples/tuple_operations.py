tup_a = (10, 20, 30)
tup_b = (40, 50, 60)
tup_c = ('alpha', 'beta', 'gamma')

# 1. Concatenation of Tuples (using the + operator)
combined_tup = tup_a + tup_b
print(f"1. Concatenated (A + B): {combined_tup}")

mixed_combined = tup_a + tup_c
print(f"   Concatenated (A + C): {mixed_combined}")

# Note: Attempting to concatenate a list and a tuple will result in an error.
# Example (will fail): combined_error = tup_a + [70, 80]

# 2. Slicing with a step
sequence_tup = tuple(range(10)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Every second element
step_2 = sequence_tup[::2]
print(f"2. Every second element [::2]: {step_2}")

# 3. Reversing the Tuple (using a negative step)
reversed_tup = sequence_tup[::-1]
print(f"3. Reversed Tuple [::-1]: {reversed_tup}")

# 4. Deleting a Tuple (del statement)
deletable_tup = (1, 2, 3)
print(f"4. Tuple before deletion: {deletable_tup}")

# The entire tuple object is removed from memory
del deletable_tup

# Uncommenting the line below will cause a NameError!
# print(f"Tuple after deletion: {deletable_tup}")
print("   Tuple 'deletable_tup' has been deleted (printing it now would cause an error).")