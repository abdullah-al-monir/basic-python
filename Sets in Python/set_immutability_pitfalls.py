# Sets are unordered and do not support indexing or direct element modification.
my_data = {'Jupiter', 'Saturn', 'Mars', 'Earth'}

# 1. Unordered Nature: Cannot access by index
try:
    print(my_data[0])
except TypeError as e:
    print(f"1. Error accessing by index: {e}")

# 2. Immutability of elements (Cannot change an item's value in place)
try:
    # Attempting to change 'Saturn' at an arbitrary 'index' (which sets don't have)
    # The error confirms that 'set' objects don't support assignment like lists do.
    my_data['Saturn'] = 'Uranus' 
except TypeError as e:
    print(f"2. Error modifying an element: {e}")

# 3. Elements must be immutable types (e.g., lists cannot be set members)
try:
    bad_set = {1, 2, ['a', 'b']}
except TypeError as e:
    print(f"3. Error: Sets cannot contain mutable objects (like lists). Reason: {e}")
    
# Valid immutable types (tuples can be members)
valid_set = {1, 2, ('a', 'b')}
print(f"   Valid Set with immutable tuple: {valid_set}")