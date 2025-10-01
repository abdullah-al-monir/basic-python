# A set is created using curly braces {} or the set() constructor.

# 1. Creating a basic set
my_set = {10, 50, 20}
print(f"1. Basic Set: {my_set}")
print(f"   Type: {type(my_set)}")
# Note: Output order is not guaranteed.

# 2. Set automatically handles duplicates
duplicates_set = {'apple', 'banana', 'apple', 'cherry', 'banana'}
print(f"2. Set with Duplicates Removed: {duplicates_set}")

# 3. Heterogeneous elements
# Sets can store different data types (strings, integers, floats, booleans)
mixed_set = {'water', 42, 9.81, True, 'fire'}
print(f"3. Heterogeneous Set: {mixed_set}")

# 4. Type Casting: List to Set
color_list = ["red", "green", "blue", "red"]
set_from_list = set(color_list)
print(f"4. Set from List (Unique Colors): {set_from_list}")

# 5. Type Casting: String to Set
set_from_string = set("programming")
print(f"5. Set from String (Unique Characters): {set_from_string}")