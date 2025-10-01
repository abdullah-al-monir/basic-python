from collections import deque

# deque (Double-Ended Queue) is optimized for quick appends and pops from both ends (O(1)).

# 1. Declaring a deque
task_queue = deque(['A', 'B', 'C'])
print(f"1. Initial Deque: {task_queue}")

# 2. Inserting Elements: append (right) and appendleft (left)
task_queue.append('D') # Add to the right end
task_queue.appendleft('Z') # Add to the left end

print(f"2. After Append Right ('D') and Append Left ('Z'): {task_queue}")

# 3. Removing Elements: pop (right) and popleft (left)
right_item = task_queue.pop() # Remove 'D' from the right
left_item = task_queue.popleft() # Remove 'Z' from the left

print(f"3. Item removed from right: {right_item}")
print(f"   Item removed from left: {left_item}")
print(f"   Deque after removals: {task_queue}")

# 4. Extending the deque
task_queue.extend(['E', 'F']) # Extend to the right
task_queue.extendleft(['Y', 'X']) # Extend to the left (note: items are inserted in reverse order)

print(f"4. After extending (right and left): {task_queue}")