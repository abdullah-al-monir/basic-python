# A tuple is created by placing all the items inside parentheses (), separated by commas.

# 1. Creating an empty tuple
empty_tup = ()
print(f"1. Empty Tuple: {empty_tup}")

# 2. Creating a tuple with strings and integers (Heterogeneous)
mixed_data_tup = (10, 'apple', 3.14, True)
print(f"2. Mixed Data Tuple: {mixed_data_tup}")

# 3. Creating a tuple from a list
data_list = ['red', 'green', 'blue']
tup_from_list = tuple(data_list)
print(f"3. Tuple from List: {tup_from_list}")

# 4. Creating a tuple from an iterable (a string)
tup_from_string = tuple('Hello')
print(f"4. Tuple from String: {tup_from_string}")

# 5. Creating a nested tuple (tuples containing other data structures)
nested_tup = (
    (1, 2),          # Another tuple
    [3, 4],          # A list
    {'key': 'value'} # A dictionary
)
print(f"5. Nested Tuple: {nested_tup}")

# 6. Creating a tuple with repetition
repeated_tup = ('star',) * 4
print(f"6. Repeated Tuple: {repeated_tup}")