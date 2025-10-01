# A generator function uses 'yield' and returns an iterator object upon call.

def simple_countdown(start_num):
    """Generates numbers counting down from start_num to 1."""
    print(f"--- Generator function initiated at {start_num} ---")
    current = start_num
    while current >= 1:
        # 'yield' pauses execution, returns the value, and saves the state (current variable)
        yield current
        current -= 1
        print(f"--- State saved, preparing for next yield (current={current}) ---")
    
    # Execution automatically finishes when the function ends, implicitly raising StopIteration.
    print("--- Countdown finished ---")

# Calling the function returns a generator object (an iterator)
countdown_generator = simple_countdown(3)

print("1. Manual Consumption using next()")
print(f"Next value: {next(countdown_generator)}")
print(f"Next value: {next(countdown_generator)}")

print("\n2. Consumption using a for loop (automatically calls next() and handles StopIteration)")
for num in countdown_generator:
    print(f"Loop value: {num}")

# The generator finishes after the loop.