# Frozensets are immutable versions of sets. Once created, they cannot be modified.

# 1. Creating a normal set
mutable_set = {'x', 'y', 'z'}
print(f"1. Normal Set: {mutable_set}")

# 2. Creating a frozenset
frozen_set = frozenset(['a', 'b', 'c'])
print(f"2. Frozenset: {frozen_set}")
print(f"   Type: {type(frozen_set)}")

# 3. Attempting to modify a frozenset (will fail)
try:
    frozen_set.add('d')
except AttributeError as e:
    print(f"3. Cannot add to frozenset. Error: {e}")

# 4. Use case: Frozensets as dictionary keys or set members
# Since frozensets are immutable, they can be used as keys in a dictionary
# or elements in another set (which a normal mutable set cannot).

# Using a frozenset as a dictionary key
my_dict = {
    frozenset({'red', 'blue'}): 'Primary Colors',
    frozenset({'green', 'orange'}): 'Secondary Colors'
}
print(f"4. Dictionary lookup using a frozenset key:")
print(f"   Lookup: {my_dict[frozenset(['blue', 'red'])]}")