# Python uses 'object interning' for small immutable objects to optimize memory usage.

# 1. Small Integers (-5 to 256) are interned.
# Both variables point to the same memory address.
val_1 = 100
val_2 = 100

print("1. Small Integer Interning (100):")
print(f"   ID of val_1: {id(val_1)}")
print(f"   ID of val_2: {id(val_2)}")
print(f"   Are IDs the same? {id(val_1) == id(val_2)}") # True

# 2. Large Integers are typically NOT interned (unless loaded at compile time).
# New objects are created for each assignment, thus different memory addresses.
val_3 = 500
val_4 = 500

print("\n2. Large Integer (500):")
print(f"   ID of val_3: {id(val_3)}")
print(f"   ID of val_4: {id(val_4)}")
print(f"   Are IDs the same? {id(val_3) == id(val_4)}") # False (or True, depending on interpreter/REPL optimization)

# 3. Immutability in action: Changing 'val_1' creates a NEW object.
original_id = id(val_1)
val_1 += 1 # val_1 now points to a new object (101)

print("\n3. Changing a variable creates a new object:")
print(f"   ID of original 100 object: {original_id}")
print(f"   ID of new 101 object (val_1): {id(val_1)}")
print(f"   Did ID change? {original_id != id(val_1)}") # True