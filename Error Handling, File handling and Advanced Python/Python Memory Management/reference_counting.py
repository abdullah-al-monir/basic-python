import sys

# Reference Counting is Python's primary memory management technique.
# Every object tracks how many variables (references) point to it.

class ExampleObject:
    def __init__(self, name):
        self.name = name
        print(f"Object '{self.name}' created.")
        
    def __del__(self):
        # This method is called when the object is about to be garbage collected (ref count drops to 0)
        print(f"Object '{self.name}' destroyed.")

# Create an object (Reference Count = 1)
data = ExampleObject("Data_A") 

# Check the reference count (sys.getrefcount counts the reference passed to the function, so result is 2)
print(f"\n1. Initial Ref Count (data): {sys.getrefcount(data) - 1}") 

# 1. Creating a new reference (Reference Count = 2)
alias = data
print(f"2. Ref Count after 'alias = data': {sys.getrefcount(data) - 1}") 

# 2. Deleting a reference (Reference Count = 1)
del alias
print(f"3. Ref Count after 'del alias': {sys.getrefcount(data) - 1}") 

# 3. Deleting the final reference (Reference Count = 0)
print("\n4. Deleting final reference 'data'...")
del data 
# The object is now freed from memory, triggering __del__.