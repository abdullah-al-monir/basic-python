from collections import defaultdict

# defaultdict allows dictionary access without worrying about missing keys,
# by providing a default value factory.

# 1. Using defaultdict with 'int' to count items
# Default value for new keys will be 0
item_list = ['pen', 'pencil', 'eraser', 'pen', 'pencil', 'pen']
inventory_count = defaultdict(int)

for item in item_list:
    inventory_count[item] += 1 # If 'item' is new, it starts at 0, then increments.

print(f"1. Inventory Counts (defaultdict with int): {inventory_count}")

# 2. Using defaultdict with 'list' to group items
# Default value for new keys will be []
student_data = [
    ('Math', 'Alice'), ('Science', 'Bob'), 
    ('Math', 'Charlie'), ('Science', 'Alice')
]
class_roster = defaultdict(list)

for subject, student in student_data:
    class_roster[subject].append(student) # If 'subject' is new, it starts as [], then appends.

print(f"2. Students Grouped by Subject (defaultdict with list):")
print(class_roster)

# 3. Accessing a missing key (no KeyError raised)
print(f"3. Attempting to access 'History' (missing key): {class_roster['History']}")
print(f"   Note: 'History' is now in the dictionary with an empty list: {class_roster}")