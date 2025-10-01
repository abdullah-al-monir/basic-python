# Python Exception Handling 🛡️

Exception handling is a mechanism that allows Python programs to gracefully manage unexpected events and errors that occur during runtime, preventing the program from crashing.

## Key Concepts

* **Error vs. Exception:** **Errors** (like `SyntaxError`) are serious problems that typically stop execution immediately. **Exceptions** (like `ZeroDivisionError`) occur at runtime and *can* be caught and handled.
* **Keywords:** The four main keywords are `try`, `except`, `else`, and `finally`.
* **Custom Exceptions:** Developers can create application-specific exceptions for clarity and precise error management.

## Files Overview

| File | Topic | Description |
| :--- | :--- | :--- |
| `basic_try_except.py` | Basic Handling | Demonstrates the core `try` and `except` blocks. |
| `try_except_else_finally.py` | Full Syntax | Shows the usage of all four keywords for complete control flow. |
| `specific_and_multiple_exceptions.py` | Targeted Catching | Handles specific exceptions and uses a single block for multiple types. |
| `raising_exceptions.py` | Raising Exceptions | Uses the `raise` keyword to manually trigger built-in exceptions. |
| `custom_exceptions.py` | Custom Exceptions | Defines and uses a custom exception class for application-specific errors. |