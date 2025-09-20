# -----------------------------------------------------------------------------
# Description: Shows how to customize the string representation of an object
#              using the __str__() method.
# -----------------------------------------------------------------------------

# 1. The __str__() Method
# The __str__() method is a special method in Python that is used to define
# a custom, human-readable string representation of an object.
# It is automatically called by the 'print()' function or when the 'str()'
# function is used on an object.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method is called to get the string representation of the object.
    def __str__(self):
        return f"This dog's name is {self.name} and they are {self.age} years old."


# 2. Creating Objects and Printing Them
# Now when we print the objects, our custom __str__ method is used,
# providing a much more readable output than the default.
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)
print(dog2)

# Expected Output:
# This dog's name is Buddy and they are 3 years old.
# This dog's name is Charlie and they are 5 years old.
