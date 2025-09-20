# -----------------------------------------------------------------------------
# Description: Demonstrates method overriding, where a subclass provides its
#              own implementation of a method from its superclass.
# -----------------------------------------------------------------------------

# 1. Parent Class (Superclass)
# This is the base class that contains a method to be overridden.
class Animal:
    def sound(self):
        print("Some generic animal sound")


# 2. Child Class (Subclass)
# This class inherits from the 'Animal' class.
class Dog(Animal):
    # Method Overriding:
    # We define a method with the same name as the one in the parent class.
    # This new implementation will be used instead of the parent's when called
    # on a 'Dog' object.
    def sound(self):
        print("Woof")


# 3. Using the Overridden Method
# When we create an instance of the 'Dog' class and call the 'sound' method,
# the overridden version in the 'Dog' class is executed.
dog = Dog()
dog.sound()

# For comparison, let's create an instance of the parent class.
animal = Animal()
animal.sound()


# Expected Output:
# Woof
# Some generic animal sound
