# -----------------------------------------------------------------------------
# Description: Demonstrates how to format strings and check for substrings.
# -----------------------------------------------------------------------------

# Using f-strings (formatted string literals)
language = "Python"
version = "3.10"
formatted_fstring = f"{language} is a high-level programming language."
print(f"F-string: {formatted_fstring}")
print(f"With multiple variables: {language} version {version} is great.")

# Using the .format() method
formatted_format = "{} is a very versatile language.".format(language)
print(f".format() method: {formatted_format}")

# Using the `in` keyword for membership testing
sentence = "The quick brown fox jumps over the lazy dog."
print(f"'fox' in sentence: {'fox' in sentence}")
print(f"'cat' in sentence: {'cat' in sentence}")
