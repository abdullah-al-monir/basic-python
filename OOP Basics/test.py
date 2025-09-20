def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        return x
    return inner


closure = outer()
print(closure())
print(closure())

def fun(a,b = []):
    b.append(a)
    return b
  
print(fun(1))
print(fun(2))

li = [1,2,3,4,5]
li.pop(2)
print(li)