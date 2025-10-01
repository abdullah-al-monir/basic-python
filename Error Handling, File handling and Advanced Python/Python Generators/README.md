# Python Generators ✨

**Generators** are functions that act as **iterators** but are defined using the `yield` keyword instead of `return`. They are essential for memory-efficient and lazy evaluation, especially when dealing with large datasets or infinite sequences.

## Key Concepts

* **`yield` vs `return`**: `yield` pauses execution and saves the function's state; `return` terminates the function.
* **Lazy Evaluation**: Values are computed and produced only when requested by `next()`.
* **Syntax**: Defined either as a generator function (`def` with `yield`) or a generator expression (`(...)`).

## Files Overview

| File | Focus Area | Description |
| :--- | :--- | :--- |
| `generator_function.py` | Generator Functions | Illustrates state-saving and lazy evaluation using `yield` in a standard function definition. |
| `yield_vs_return.py` | Comparison | Provides a direct comparison demonstrating the state difference between `yield` and `return`. |
| `generator_expression.py` | Concise Syntax | Shows the memory-efficient, single-line alternative to list comprehensions. |
| `large_data_example.py` | Real-World Application | Simulates the use of generators for processing large data without excessive memory usage. |