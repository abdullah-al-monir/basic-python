# Python Collections Module ✨

The `collections` module provides specialized, high-performance container datatypes that extend the functionality of Python's built-in containers (like `dict`, `list`, and `tuple`). These classes are essential for writing clean, efficient, and readable code for specific data structure needs.

## Specialized Containers Covered

| File | Container | Description |
| :--- | :--- | :--- |
| `counter.py` | `Counter` | A dictionary subclass for counting hashable objects (like a bag or multiset). |
| `ordereddict.py` | `OrderedDict` | A dictionary subclass that remembers the order of key insertion, with order-sensitive methods. |
| `defaultdict.py` | `defaultdict` | A dictionary subclass that calls a factory function to supply missing values. |
| `namedtuple.py` | `namedtuple` | Factory function for creating tuple subclasses with named fields. |
| `deque.py` | `deque` | List-like container optimized for fast appends and pops from both ends (Doubly Ended Queue). |
| `chainmap.py` | `ChainMap` | A class that groups multiple dictionaries or other mappings into a single view. |
| `user_wrappers.py` | `UserDict`, `UserList`, `UserString` | Base classes for wrapping dictionary, list, and string objects to create custom containers. |