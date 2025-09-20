# -----------------------------------------------------------------------------
# Description: Explains the difference between static methods and class methods.
# -----------------------------------------------------------------------------

# 1. Static Methods
# Static methods are methods that belong to the class but do not need access
# to the instance or the class itself. They are defined using the `@staticmethod`
# decorator and do not take 'self' or 'cls' as their first argument.
# They are typically used for utility functions that relate to the class.

# 2. Class Methods
# Class methods are methods that are bound to the class, not the instance.
# They take the class itself as their first argument, conventionally named 'cls'.
# They are defined using the `@classmethod` decorator. They are often used
# to create factory methods or methods that operate on class-level data.

class Dog:
    @staticmethod
    def info():
        # This method is static. It does not access any instance or class data.
        print("Dogs are loyal animals.")

    @classmethod
    def count(cls):
        # This method is a class method. It receives the class itself ('cls').
        # It can be used to access or modify class attributes.
        print(f"This is a method of the class: {cls.__name__}")


# 3. Calling the Methods
# We can call both static and class methods from an instance or directly from
# the class itself.
dog_instance = Dog()

# Calling the static method via an instance and the class
dog_instance.info()
Dog.info()

# Calling the class method via an instance and the class
dog_instance.count()
Dog.count()


# Expected Output:
# Dogs are loyal animals.
# Dogs are loyal animals.
# This is a method of the class: Dog
# This is a method of the class: Dog
