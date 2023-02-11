from math import *

a = int(input())
b = int(input())
dx = float(input())
x = a
count = 0

def f(x):
    y = (x**2)*(e**(sin(x) + cos(x)))
    return y

def average_arithmetic(a, b, dx):
    x = [a + i * dx for i in range(int((b-a)/dx) + 1)]
    y = [f(xi) for xi in x]
    average_arithmetic = sum(y) / len(y)
    return round(average_arithmetic, 3)

def average_geometric(a, b, dx):
    x = [a + i * dx for i in range(int((b-a)/dx) + 1)]
    y = [f(xi) for xi in x]
    product = 1
    for yi in y:
        product *= yi
    average_geometric = pow(product, 1/len(y))

    return round(average_geometric, 3)

while x <= b:
    y = f(x)
    count += 1
    print("x =", x, "y =", y)
    x += dx

arithmetic_mean = average_arithmetic(a, b, dx)
print("Arithmetic mean:", arithmetic_mean)

geometric_mean = average_geometric(a, b, dx)
print("Geometric mean:", geometric_mean)