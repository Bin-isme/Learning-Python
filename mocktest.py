from math import *
from numpy import *
from random import *
def function(x):
    return 1 + 1/(1+exp(-x))
def compute_PI_recursion(i):
    if i > 0:
        return ((-1)**(i+1))/(2*i-1) + compute_PI_recursion(i-1)
    else:
        return 0
def compute_PI_loop(n):
    result = 0
    for i in arange(1,n+1):
        result += ((-1)**(i+1))/(2*i-1)
    return 4*result
def softmax(array):
    softmax_array = [0]*len(array)
    sum = 0
    for i in array:
        sum += exp(i)
    for i in range(len(array)):
        softmax_array[i] = exp(array[i]) / sum
    return softmax_array
def find_max(array):
    max1 = array[0];
    for i in array:
        if max1 < i:
            max1 = i
    return max1
def softmax_memoryproblem(array):
    max1 = find_max(array)
    softmax_array = [0]*len(array)
    sum = 0.0
    for i in array:
        sum += exp(i-max1)
    for i in range(len(array)):
        softmax_array[i] = exp(array[i]-max1) / sum
    return softmax_array
def print_array(array):
    for i in range(len(array)):
        array[i] = randint(0,9)
    return array
def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum
def print_another_array(n):
    array = []
    for i in range(n):
        array.append(randint(0,9))
    return array
array = [x for x in range(5)]
array = print_array(array)
print(array)
print(sum_array(array))
another_array = print_another_array(5)
print(another_array)
print(sum_array(another_array))

