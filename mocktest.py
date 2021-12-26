from math import *
def function(x):
    return 1 + 1 / (1 + exp(-x))
def function1(x):
    if x > 0:
        return (((-1)**(x+1) / (2*x-1)) + function1(x-1))
    else:
        return 0
def function11(x):
    result = 0
    for i in range(1,x+1):
        result += ((-1)**(i+1))/(2*i-1)
    return 4*result
def function2(x):
    Pi = 0
    for i in range(x+1):
        Pi += (-1)**(i) / ((2*i+2)*(2*i+3)*(2*i+4))
    Pi = 3 + 4*Pi
    return Pi
def function22(x):
    if x >= 0:
        return (pow(-1,x) / ((2*x+2)*(2*x+3)*(2*x+4)) + function22(x-1))
    else:
        return 0
print(function(0))
print(4*function1(100))
print(function11(100))
print(function2(100))
print(3 + 4*function22(100))