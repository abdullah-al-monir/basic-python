# Demonstrates the crucial difference in behavior: state pausing vs. function termination.

# 1. Function using RETURN (Terminates immediately)
def multiply_and_return(data):
    total = 1
    for x in data:
        total *= x
    return total # Function terminates here; a single value is returned

result_return = multiply_and_return([2, 3, 4])
print(f"1. RETURN result (single value): {result_return}") 
# Output: 24 (2*3*4)

# 2. Function using YIELD (Pauses and retains state)
def multiply_and_yield(data):
    total = 1
    for x in data:
        total *= x
        # Execution pauses, sends 'total' out, and waits for the next() call
        yield total
    # Function finishes only when the last yield is processed

# Create the generator object
generator_obj = multiply_and_yield([2, 3, 4])

print("\n2. YIELD result (sequence of values):")
print(f"  First step (2): {next(generator_obj)}")
print(f"  Second step (2*3): {next(generator_obj)}")
print(f"  Third step (6*4): {next(generator_obj)}")

# Key Takeaway: 'return' gives a final result; 'yield' gives intermediate results.