# -----------------------------------------------------------------------------
# Description: Demonstrates the 'self' parameter for accessing object attributes
#              and methods from within the class.
# -----------------------------------------------------------------------------

# 1. The `self` Parameter
# In Python, 'self' is a convention (not a keyword) that refers to the instance
# of the class. It is the first argument in every instance method, including
# the __init__ constructor. It allows a method to access the attributes and
# other methods of the object it belongs to.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is an instance method. The 'self' parameter gives it access
    # to the instance's attributes (like self.name).
    def bark(self):
        print(f"{self.name} is barking!")


# 2. Creating and Using an Object
# When an object's method is called, Python automatically passes the object
# itself as the 'self' argument.
dog1 = Dog("Buddy", 3)

# Calling the 'bark' method on the 'dog1' object.
# The 'dog1' object is passed as the 'self' argument.
dog1.bark()


# Expected Output:
# Buddy is barking!
