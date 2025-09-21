# -----------------------------------------------------------------------------
# Description: Examples of useful built-in string methods.
# -----------------------------------------------------------------------------

my_string = "  Python is awesome  "

# len(): returns the length of the string
print(f"Length of the string: {len(my_string)}")

# upper() and lower(): convert case
print(f"Uppercase: {my_string.upper()}")
print(f"Lowercase: {my_string.lower()}")

# strip(): removes leading and trailing whitespace
print(f"Stripped: '{my_string.strip()}'")

# replace(): replaces a substring with another
print(f"Replaced: {my_string.replace('awesome', 'powerful')}")
