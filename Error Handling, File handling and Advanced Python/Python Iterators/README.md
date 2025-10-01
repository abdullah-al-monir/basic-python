# Python Iterators 🔄

An **Iterator** is an object that represents a stream of data. It is the fundamental mechanism Python uses to power `for` loops and other sequence traversals. Iterators are memory-efficient because they adhere to **lazy evaluation**, yielding items one at a time.

## The Iterator Protocol

An object must implement the **Iterator Protocol** to be considered an iterator. This protocol requires two methods:

1.  **`__iter__()`**: Returns the iterator object itself.
2.  **`__next__()`** (or `next()` in Python 2): Returns the next element of the sequence. Raises `StopIteration` when no more elements are available.

## Files Overview

| File | Topic | Description |
| :--- | :--- | :--- |
| `iterator_basics.py` | Built-in Iterators | Demonstrates the core `iter()` and `next()` functions on standard Python iterables. |
| `custom_iterator_class.py` | Custom Implementation | Creates a class that implements the `__iter__` and `__next__` methods to iterate over a custom sequence. |
| `stop_iteration_handling.py` | Exhausting an Iterator | Focuses on the `StopIteration` exception and how it signals the end of the sequence. |
| `iterable_vs_iterator.py` | Distinction | Clarifies the difference between an **iterable** (can produce an iterator) and an **iterator** (consumes the data). |