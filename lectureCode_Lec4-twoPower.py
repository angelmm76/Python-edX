# From Lecture 4, How Environments Separate Variable Bindings
x= 2

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x

print twoPower(x,6)