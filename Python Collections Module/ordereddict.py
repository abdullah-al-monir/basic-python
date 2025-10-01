from collections import OrderedDict

# OrderedDict preserves the original insertion order of keys.

# 1. Creating a regular dictionary (Modern Python 3.7+ preserves order, but less feature-rich)
regular_dict = {}
regular_dict['first'] = 101
regular_dict['second'] = 202
regular_dict['third'] = 303
print("1. Regular Dict Insertion Order:")
for k, v in regular_dict.items():
    print(f"   {k}: {v}")

# 2. Creating an OrderedDict
ordered_data = OrderedDict()
ordered_data['alpha'] = 1
ordered_data['beta'] = 2
ordered_data['gamma'] = 3
ordered_data['delta'] = 4
print("\n2. OrderedDict Insertion Order:")
for k, v in ordered_data.items():
    print(f"   {k}: {v}")

# 3. Deleting and Re-inserting a key
# Re-insertion moves the key to the end, which is a key feature of OrderedDict.
print("\n3. Before deletion and re-insertion:")
print(list(ordered_data.keys()))

# Delete an element
ordered_data.pop('alpha') 

# Re-insert the same key
ordered_data['alpha'] = 1 

print("   After re-inserting 'alpha':")
print(list(ordered_data.keys())) # 'alpha' is now at the end