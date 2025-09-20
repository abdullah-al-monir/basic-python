# -----------------------------------------------------------------------------
# Description: Demonstrates how to use property decorators (@property) to create
#              getter and setter methods for controlled attribute access.
# -----------------------------------------------------------------------------

# 1. Encapsulation and Property Decorators
# Encapsulation is the principle of bundling data and the methods that operate on
# that data into a single unit (an object). It is often used to restrict direct
# access to attributes. In Python, we use a convention of a leading underscore
# (e.g., _name) for "private" attributes, and we use `@property` decorators to
# create controlled access via getter and setter methods.

class Dog:
    def __init__(self, name, age):
        self._name = name  # Conventionally private variable
        self._age = age    # Conventionally private variable

    # Getter for 'name'
    # The '@property' decorator makes this method behave like a read-only attribute.
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    # The '@name.setter' decorator allows us to set the 'name' attribute.
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for 'age'
    @property
    def age(self):
        return self._age

    # Setter for 'age' with validation
    # We can add logic here to validate the new value before setting it.
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be a negative number!")
        else:
            self._age = value


# 2. Using the Getter and Setter Methods
dog1 = Dog("Buddy", 3)

# Using the getter to retrieve the name (looks like accessing an attribute)
print(f"Original name: {dog1.name}")

# Using the setter to update the name
dog1.name = "Max"
print(f"New name after setting: {dog1.name}")

# Using the age setter with a valid value
dog1.age = 4
print(f"New age after setting: {dog1.age}")

# Using the age setter with an invalid value
dog1.age = -1
print(f"Age after failed set attempt: {dog1.age}")


# Expected Output:
# Original name: Buddy
# New name after setting: Max
# New age after setting: 4
# Age cannot be a negative number!
# Age after failed set attempt: 4
