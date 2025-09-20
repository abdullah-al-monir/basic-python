# -----------------------------------------------------------------------------
# Description: Demonstrates how to define an abstract class and an abstract
#              method, which must be implemented by subclasses.
# -----------------------------------------------------------------------------

# 1. Abstract Classes
# An abstract class is a blueprint for other classes. It cannot be instantiated
# directly. It is designed to be inherited from, and it may contain one or more
# abstract methods. Abstract classes are created using the 'abc' module.

from abc import ABC, abstractmethod

# The ABC class is the metaclass for creating abstract base classes.
class Animal(ABC):
    # Abstract Method:
    # An abstract method is a method that is declared in an abstract class
    # but has no implementation. It must be overridden (implemented) by any
    # concrete subclass.
    @abstractmethod
    def sound(self):
        # The 'pass' keyword is used here because the method has no body.
        pass

# 2. Creating a Subclass
# This subclass inherits from the abstract 'Animal' class.
class Dog(Animal):
    # To be a valid concrete class, 'Dog' must provide an implementation
    # for the abstract 'sound' method.
    def sound(self):
        print("Woof")


# 3. Using the Concrete Subclass
# We can now create an instance of the 'Dog' class, which is a concrete
# implementation of 'Animal'.
dog = Dog()
dog.sound()

# If we try to instantiate the abstract class directly, it will raise an error.
# For example, uncommenting the line below will cause an error:
# animal = Animal()
# print(animal)


# Expected Output:
# Woof
