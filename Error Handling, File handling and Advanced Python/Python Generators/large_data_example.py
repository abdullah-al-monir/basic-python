# Generators are vital for processing large or simulated infinite data streams 
# because they never hold the full sequence in memory.

def get_data_stream(limit):
    """Simulates reading data records one at a time from a large source."""
    for i in range(1, limit + 1):
        # Pretend this is reading one line from a massive file
        record = f"Record_{i}" 
        print(f"  [Generator] Yielding {record}...")
        yield record
        
# 1. Processing Pipeline using the generator
# We can process millions of records without needing memory for all of them.
RECORD_LIMIT = 5 # Small limit for demonstration
records_to_process = get_data_stream(RECORD_LIMIT)

print(f"1. Starting processing for {RECORD_LIMIT} records...")
processed_count = 0

for record in records_to_process:
    # Processing happens immediately after each yield
    print(f"  [Processor] Processing {record}...")
    processed_count += 1
    
    if processed_count == 3:
        # We can stop processing early without wasting computation on the rest.
        print("\n2. Stopping early after 3 records.")
        break

# Key Benefit: The memory usage remains constant, regardless of RECORD_LIMIT's size.