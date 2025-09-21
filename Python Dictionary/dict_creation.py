# -----------------------------------------------------------------------------
# Description: Demonstrates how to create dictionaries in Python.
# -----------------------------------------------------------------------------

# A dictionary can be created with curly braces {}.
# It stores key-value pairs.
car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(f"Dictionary created with curly braces: {car_details}")

# Values can be of any data type, and keys must be immutable.
mixed_dict = {
    1: "first",
    "second": 2,
    (1, 2): ["one", "two"],
    True: "yes"
}
print(f"Dictionary with mixed keys and values: {mixed_dict}")

# A dictionary can also be created using the dict() constructor.
movie_ratings = dict(
    Inception=8.8, 
    Parasite=8.6, 
    Dune=8.0
)
print(f"Dictionary created with dict() constructor: {movie_ratings}")
