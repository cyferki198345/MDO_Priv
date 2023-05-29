import numpy

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ValueError("Dzielenie przez 0")
    return a/b

def mean(numbers):
    return numpy.mean(numbers)