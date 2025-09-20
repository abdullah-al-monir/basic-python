# -----------------------------------------------------------------------------
# Description: Demonstrates the fundamental concepts of Python classes and objects.
# -----------------------------------------------------------------------------

# 1. Defining a Class
# A class is a blueprint for creating objects. It bundles data (attributes) and
# functions (methods) together into a single unit.
# The 'class' keyword is used to define a new class, followed by the class name.

class Dog:
    # Class Attribute:
    # A class attribute is a variable that is shared by all instances of the class.
    # It is defined directly inside the class but outside of any methods.
    sound = "bark"


# 2. Creating an Object
# An object is a specific instance of a class. It represents a real-world entity
# and holds its own unique data. Creating an object is also called instantiation.
# To create an object, you call the class name as if it were a function.

dog1 = Dog()

# 3. Accessing Class Attributes
# Attributes can be accessed using the dot (.) operator.
# Since 'sound' is a class attribute, we can access it from the object instance.
print(f"Dog 1's sound is: {dog1.sound}")

# You can also access the class attribute directly from the class itself.
print(f"The general sound of a Dog class is: {Dog.sound}")


# Expected Output:
# Dog 1's sound is: bark
# The general sound of a Dog class is: bark
