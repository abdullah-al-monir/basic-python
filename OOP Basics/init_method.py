# -----------------------------------------------------------------------------
# Description: Explains the use of the __init__() method, the Python constructor.
# -----------------------------------------------------------------------------

# 1. The __init__ Method
# The __init__() method is a special function known as the constructor.
# It is automatically called when a new object is created from a class.
# It is used to initialize the object's attributes with the values passed to it.

class Dog:
    # Class attribute shared by all instances
    species = "Canine"

    # The __init__ method initializes instance attributes.
    # 'self' is a reference to the current instance of the class.
    # 'name' and 'age' are parameters for the constructor.
    def __init__(self, name, age):
        # Instance attributes:
        # These are unique to each object. 'self.name' and 'self.age'
        # will store the values passed in during object creation.
        self.name = name
        self.age = age


# 2. Creating an Object with __init__()
# When we create an object, we pass arguments that correspond to the
# parameters of the __init__ method.
dog1 = Dog("Buddy", 3)

# 3. Accessing Attributes
# We can now access both the instance attributes and the class attributes
# from the newly created object.
print(f"Dog's name: {dog1.name}")
print(f"Dog's age: {dog1.age}")
print(f"Dog's species: {dog1.species}")


# Expected Output:
# Dog's name: Buddy
# Dog's age: 3
# Dog's species: Canine
