# Python memory is conceptually divided into Stack (references) and Heap (objects/values).

def process_data_unit(data_list):
    # This function call frame and its local variables are stored in the STACK.
    
    # 'data_list' is a reference variable stored on the STACK.
    # It points to the actual list object stored on the HEAP.
    
    # 'local_count' is a small immutable object reference stored on the STACK.
    local_count = 0
    
    for item in data_list:
        # 'item' is a reference variable stored on the STACK for each loop iteration.
        local_count += item
    
    print(f"Function executed. Final count (STACK data): {local_count}")
    # When the function ends, the stack frame and 'local_count' are automatically freed.

# --- Global Scope ---

# 1. HEAP Allocation: The actual list data is allocated in HEAP memory.
large_dataset = [10, 20, 30, 40, 50] 

# 2. STACK Allocation: 'large_dataset' is a reference variable stored on the STACK,
# pointing to the list object in the HEAP.
print("1. The list data is in the HEAP.")
print("2. 'large_dataset' is a pointer/reference in the STACK.")
print(f"   Memory ID of the list object: {id(large_dataset)}")

# 3. Function Call
print("\n3. Calling function (new STACK frame created)...")
process_data_unit(large_dataset) 

# 4. Persistence: The HEAP object still exists after the function call ends.
print("4. Back in global scope.")
print(f"   The object {large_dataset} (in HEAP) is still alive.")