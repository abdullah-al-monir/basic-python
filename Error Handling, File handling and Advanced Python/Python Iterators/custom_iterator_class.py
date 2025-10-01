# Creating a custom iterator that yields descending positive integers starting from N.

class CountdownIterator:
    """An iterator that counts down from a specified number N to 1."""
    
    def __init__(self, start):
        # Initialize the starting value (the state of the iterator)
        self.current = start
        
    def __iter__(self):
        # The __iter__ method must return the iterator object itself.
        return self
        
    def __next__(self):
        # 1. Check if the sequence is finished
        if self.current <= 0:
            raise StopIteration
            
        # 2. Get the current value to yield
        value = self.current
        
        # 3. Update the state for the next call
        self.current -= 1
        
        # 4. Return the value
        return value

# --- Usage Example ---
# Create an instance (iterable)
countdown = CountdownIterator(5)

# Get the iterator object from the instance
it = iter(countdown)

print("Counting down from 5:")
print(next(it))
print(next(it))
print(next(it))

# The rest can be consumed using a loop
print("\nRemaining items:")
for item in it:
    print(item)