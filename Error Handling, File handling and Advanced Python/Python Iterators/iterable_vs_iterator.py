# Clarifying the distinction between an Iterable (can be iterated over) 
# and an Iterator (the object that performs the iteration).

# 1. Iterable: The source collection (list)
book_pages = [10, 20, 30, 40]
print(f"1. Iterable (list): {book_pages}")
print(f"   Can be passed to iter(): {hasattr(book_pages, '__iter__')}") # True
print(f"   Can be passed to next(): {hasattr(book_pages, '__next__')}") # False

# 2. Iterator: The object returned by iter()
page_iterator_1 = iter(book_pages)
print(f"\n2. Iterator 1 (from list): {page_iterator_1}")
print(f"   Can be passed to iter(): {hasattr(page_iterator_1, '__iter__')}") # True
print(f"   Can be passed to next(): {hasattr(page_iterator_1, '__next__')}") # True

# 3. Key Difference: Iterators are stateful and get consumed.
print(f"\n3. Consuming Iterator 1: {next(page_iterator_1)}, {next(page_iterator_1)}")
# Iterator 1 is now at the third element.

# 4. Creating a second, independent iterator from the same iterable
page_iterator_2 = iter(book_pages)
print(f"\n4. Iterator 2 (new): {page_iterator_2}")

# Iterator 2 starts from the beginning, independent of Iterator 1's state
print(f"   Consuming Iterator 2: {next(page_iterator_2)}")

# Summary:
# - The **Iterable** (`book_pages`) is the reusable blueprint.
# - The **Iterator** (`page_iterator_1`, `page_iterator_2`) is the one-time-use traveler that holds the current position.