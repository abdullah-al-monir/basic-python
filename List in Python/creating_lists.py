# -----------------------------------------------------------------------------
# Description: Demonstrates different methods for creating lists.
# -----------------------------------------------------------------------------

# Using square brackets [] to create a list directly
numbers = [10, 20, 30, 40]
print(f"List of numbers: {numbers}")

# A list can contain different data types
mixed_list = ["book", 123, True, 5.5]
print(f"Mixed data types: {mixed_list}")

# Using the list() constructor with an iterable
from_string = list("PYTHON")
print(f"List from a string: {from_string}")

# Creating a list with repeated elements using the multiplication operator
repeated_zeros = [0] * 5
print(f"List with repeated zeros: {repeated_zeros}")

# Creating a list from a tuple
from_tuple = list((1, 2, 3))
print(f"List from a tuple: {from_tuple}")

# Length of a list
length = len(numbers)
print(f"Length of the list: {length}")
