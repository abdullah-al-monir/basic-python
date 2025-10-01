# Garbage Collection (GC) handles objects that still have a reference count > 0 
# but are unreachable due to circular references.

import gc

# Force GC to run immediately to see its effect clearly
gc.collect() 

# Define a class where two instances can refer to each other
class Link:
    def __init__(self, value):
        self.value = value
        self.other = None
        
    def __del__(self):
        print(f"Link object '{self.value}' destroyed.")

# 1. Create two objects that reference each other (a circular reference)
print("1. Creating circular references:")
node_a = Link("A")
node_b = Link("B")

node_a.other = node_b # A references B
node_b.other = node_a # B references A

# 2. Delete the external references
# Ref count for both node_a and node_b drops to 1 (due to the circular link).
# Standard reference counting *cannot* free these objects yet.
print("\n2. Deleting external references (a and b):")
del node_a
del node_b

# 3. Running the Garbage Collector
# The GC detects that these remaining objects are unreachable from the rest of the program
# and frees them, breaking the cycle.
print("\n3. Running explicit garbage collection...")
collected = gc.collect()
print(f"   Collected {collected} unreachable objects.")