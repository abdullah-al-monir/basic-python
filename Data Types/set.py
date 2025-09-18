set1 = set()

set1 = set("Python World")

print("Set with the use of String: ", set1)

set2 = ["Python", "World"]

print("Set with the use of List: ", set(set2))

for i in set2:
    print(i, end=" ")

print('\n')
print("Python" in set2)
