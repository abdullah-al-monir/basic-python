# For loops is used to iterate over a sequence such as a list, tuple, string or range. It allow to execute a block of code repeatedly, once for each item in the sequence.

x = 5
for i in range(x):
    print(i)

# list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# tuple
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)


# string
for x in "banana":
    print(x)

# dictionary
fruits = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}
for x in fruits:
    print("%s is %s" % (x, fruits[x]))

# set
fruits = {"apple", "banana", "cherry"}
for x in fruits:
    print(x)
    
    