# -----------------------------------------------------------------------------
# Description: Illustrates the difference between class variables (shared) and
#              instance variables (unique to each object).
# -----------------------------------------------------------------------------

# 1. Class vs. Instance Variables
# Class Variables: Shared by all instances of the class. They are defined
#                  at the class level.
# Instance Variables: Unique to each instance (object). They are defined
#                     within methods, usually the __init__ constructor.

class Dog:
    # This is a class variable. It is shared by all Dog objects.
    species = "Canine"

    def __init__(self, name, age):
        # These are instance variables. Each object will have its own copy.
        self.name = name
        self.age = age


# 2. Creating and Accessing Variables
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing the class variable (shared) and instance variables (unique).
print(f"Dog 1's species: {dog1.species}")
print(f"Dog 1's name: {dog1.name}")
print(f"Dog 2's name: {dog2.name}")

# 3. Modifying Variables
# Modifying an instance variable on one object does not affect others.
dog1.name = "Max"
print(f"\nUpdated Dog 1's name: {dog1.name}")
print(f"Dog 2's name is still: {dog2.name}")

# Modifying a class variable via the class itself affects all instances.
Dog.species = "Feline"
print(f"\nDog 1's species is now: {dog1.species}")
print(f"Dog 2's species is also now: {dog2.species}")


# Expected Output:
# Dog 1's species: Canine
# Dog 1's name: Buddy
# Dog 2's name: Charlie
#
# Updated Dog 1's name: Max
# Dog 2's name is still: Charlie
#
# Dog 1's species is now: Feline
# Dog 2's species is also now: Feline
