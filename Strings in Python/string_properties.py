# -----------------------------------------------------------------------------
# Description: Demonstrates immutability, concatenation, and repetition.
# -----------------------------------------------------------------------------

# String Immutability
original_string = "hello world"
# Attempting to change a character will result in an error:
# original_string[0] = "H" # TypeError: 'str' object does not support item assignment

# To "update" a string, we must create a new one
updated_string = "H" + original_string[1:]
print(f"Original string: {original_string}")
print(f"Updated string: {updated_string}")

# Deleting an entire string variable
del updated_string
# Trying to access `updated_string` here would cause a NameError.

# String Concatenation (+)
first_part = "Learning "
second_part = "Python"
combined_string = first_part + second_part
print(f"Concatenated string: {combined_string}")

# String Repetition (*)
greeting = "Hi "
repeated_greeting = greeting * 4
print(f"Repeated string: {repeated_greeting}")
