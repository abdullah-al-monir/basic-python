# simple function
def call():
    print("Python World")


call()

# function with parameter


def call(name):
    print("Hello", name)


call("Python")

# function with return value


def call(name):
    return "Hello " + name


print(call("Python"))

# function with default parameter


def call(name="Python"):
    return "Hello " + name


print(call())


# function with variable length parameter
def call(*names):
    for name in names:
        print("Hello", name)


call("Python", "World")


# function with keyword parameter
def call(**names):
    for name in names.values():
        print("Hello", name)


call(name1="Python", name2="World")


# function with lambda
def f(x): return x * x


print(f(5))

# function with both types of arguments
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)


def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")


# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Hello', mid='Python', last='World')

# function within function


def outer_fun():
    s = "Python World"

    def inner_fun():
        print(s)

    inner_fun()


outer_fun()


