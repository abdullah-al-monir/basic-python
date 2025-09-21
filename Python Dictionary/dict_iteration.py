# -----------------------------------------------------------------------------
# Description: Shows how to iterate over dictionary keys, values, and items.
# -----------------------------------------------------------------------------

book_catalog = {
    "The Hobbit": "J.R.R. Tolkien",
    "1984": "George Orwell",
    "Pride and Prejudice": "Jane Austen"
}

# Iterate over keys (default behavior)
print("--- Iterating over keys ---")
for title in book_catalog:
    print(title)

# Iterate over values using .values()
print("\n--- Iterating over values ---")
for author in book_catalog.values():
    print(author)

# Iterate over both keys and values using .items()
print("\n--- Iterating over items (key, value) ---")
for title, author in book_catalog.items():
    print(f"Title: {title}, Author: {author}")

# Example using zip() for key-value iteration
print("\n--- Iterating with zip() ---")
countries = book_catalog.keys()
authors = book_catalog.values()
for country, capital in zip(countries, authors):
    print(f"The author of {country} is {capital}.")

# Unpacking a dictionary into a list of keys
print("\n--- Unpacking a dictionary ---")
keys = [*book_catalog]
print(f"Unpacked keys: {keys}")
