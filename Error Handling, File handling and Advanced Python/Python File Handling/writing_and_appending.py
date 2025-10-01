# Demonstrates writing to a file (w mode) and appending to a file (a mode).

FILE_NAME = "session_data.txt"

# 1. Writing Mode ('w'): Creates file or overwrites existing content
print("--- 1. Writing Mode ('w') ---")
with open(FILE_NAME, "w") as f:
    f.write("Session Started: 2023-10-01\n")
    f.write("User activity logged.\n")
print(f"Initial content written to '{FILE_NAME}'. (Any previous content was cleared)")

# Verification: Read the content
with open(FILE_NAME, "r") as f:
    print(f"Current content:\n{f.read().strip()}")


# 2. Appending Mode ('a'): Adds new content to the end of the file
print("\n--- 2. Appending Mode ('a') ---")
with open(FILE_NAME, "a") as f:
    f.write("User logged out.\n")
    f.write("Session Ended: 2023-10-01\n")
print(f"New data appended to '{FILE_NAME}'.")

# Final Verification: Read the complete content
with open(FILE_NAME, "r") as f:
    print(f"Final content:\n{f.read().strip()}")