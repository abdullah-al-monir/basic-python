# The StopIteration exception is the signal that an iterator is exhausted.
import re

# Use a generator expression for a simple, exhausted-on-use iterator
data_gen = (x * 2 for x in [1, 2, 3])
data_iterator = iter(data_gen)

print("--- Manual Iteration with Error Handling ---")
count = 1
while True:
    try:
        # Attempt to get the next item
        item = next(data_iterator)
        print(f"Item {count}: {item}")
        count += 1
        
    except StopIteration:
        # The exception is caught when the sequence is fully consumed
        print("\nCaught StopIteration: Sequence finished.")
        break
        
# A for loop handles the StopIteration exception implicitly.
# If we try to iterate over the exhausted iterator again:
print("\n--- Attempting to reuse the exhausted iterator ---")
re_run_count = 0
for item in data_iterator: # This loop immediately stops because the iterator is already exhausted
    re_run_count += 1
    
print(f"Items yielded in second loop: {re_run_count}") 
# Output will be 0, showing the iterator cannot be reset without creating a new one.