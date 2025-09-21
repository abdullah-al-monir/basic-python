# -----------------------------------------------------------------------------
# Description: Explains how Python lists store references to objects.
# -----------------------------------------------------------------------------

# A list storing different data types
data = [10, "Python", [1, 2], {"key": "value"}]

# Each element is a reference to a separate object in memory.
# The `id()` function returns the unique memory address of an object.
print(f"ID of the integer 10: {id(data[0])}")
print(f"ID of the string 'Python': {id(data[1])}")
print(f"ID of the nested list: {id(data[2])}")
print(f"ID of the dictionary: {id(data[3])}")

print("\n--- Immutables vs. Mutables ---")
# When we assign a new value, the reference changes.
# The original integer object is not modified, a new one is created.
num = 5
print(f"ID of initial number: {id(num)}")
num = 10
print(f"ID of new number: {id(num)}")

# But if a list contains a mutable object, that object can be modified in place.
mutable_list = data[2]
print(f"ID of mutable_list before change: {id(mutable_list)}")
mutable_list.append(3)
print(f"List after appending to mutable_list: {data}")
print(f"ID of mutable_list after change: {id(mutable_list)}")
# The ID remains the same because we modified the object, not the reference.
