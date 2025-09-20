A Guide to Python FunctionsIntroductionIn Python, a function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.This guide covers the fundamental concepts of Python functions, from declaration and calling to different types of arguments and advanced topics like recursion.Function DeclarationA function is defined using the def keyword, followed by the function name, parentheses (), and a colon :.Syntax:def function_name(parameters):
    # function body
Example:def welcome_message():
    print("Welcome to Python World Academy")
Calling a FunctionOnce a function is declared, you can execute its code by calling it. A function call consists of the function's name followed by parentheses ().Example:def welcome_message():
    print("Welcome to Python World Academy")

welcome_message() # This is the function call
Output:Welcome to Python World Academy
Function ArgumentsArguments are values passed to a function when it is called. A function can have any number of arguments, which are defined within the parentheses in the function declaration.Example:def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))
Output:Even
Odd
Types of Function ArgumentsPython supports several ways to pass arguments to a function:1. Default ArgumentsA default argument is a parameter that is given a default value in the function definition. If a value is not provided during the function call, the default value is used.Example:def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)
Output:x:  10
y:  50
2. Keyword ArgumentsValues are passed by explicitly naming the parameters. The order of the arguments in the function call doesn't matter.Example:def student(fname, lname):
    print(fname, lname)

student(fname='Python', lname='World')
student(lname='World', fname='Python')
Output:Python World
Python World
3. Positional ArgumentsArguments are assigned to parameters based on their position or order in the function call.Example:def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

nameAge("Suraj", 27)
nameAge(27, "Suraj")
Output:Hi, I am Suraj
My age is  27
Hi, I am 27
My age is  Suraj
4. Arbitrary Arguments (*args and **kwargs)These special symbols allow a function to accept a variable number of arguments.*args is used for a non-keyworded, variable-length argument list.**kwargs is used for a keyworded, variable-length argument list.Example:def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Python', mid='World', last='Academy')
Output:Non-Keyword Arguments (*args):
Hey
Welcome

Keyword Arguments (**kwargs):
first == Python
mid == World
last == Academy
Function within Functions (Nested Functions)A function defined inside another function is called an inner function. It can access variables from the enclosing function's scope.Example:def f1():
    s = 'I love Python World Academy'
    def f2():
        print(s)
        
    f2()
f1()
Output:I love Python World Academy
Anonymous Functions (Lambda)An anonymous function is a function without a name. They are created using the lambda keyword and are typically used for simple, single-expression tasks.Example:def cube(x): return x*x*x   # Traditional function
cube_l = lambda x : x*x*x   # Lambda function

print(cube(7))
print(cube_l(7))
Output:343
343
Return StatementThe return statement is used to exit a function and send a value back to the caller. If no value is specified, the function returns None.Example:def square_value(num):
    """This function returns the square value of the entered number."""
    return num**2

print(square_value(2))
print(square_value(-4))
Output:4
16
Pass by Reference vs. Pass by ValuePython uses "pass-by-object-reference." The behavior depends on the mutability of the object passed.Mutable objects (e.g., lists, dictionaries): Changes made inside the function affect the original object.Immutable objects (e.g., integers, strings, tuples): The original object remains unchanged.Example:# Modifying a mutable list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst) # list is modified

# Modifying an immutable integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a) # integer is not modified
Output:[20, 11, 12, 13]
10
Recursive FunctionsA recursive function is one that calls itself to solve a problem. It's crucial to include a base case to prevent infinite recursion.Example:def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))
Output:24
