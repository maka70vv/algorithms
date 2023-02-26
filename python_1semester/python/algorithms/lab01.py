from math import *

def f(x):
    return 2*x**2 - 5*x - 10

def dichotomy (a, b, E):
    counter = 0
    d = 0.1*E
    print("Dichotomy = ")
    while (b - a) > E:
        x1 = ((a + b) / 2) - d
        f1 = f(x1)
        x2 = ((a + b) / 2) + d
        f2 = f(x2)
        if f1 < f2:
            b = x2
        if f1 >= f2:
            a = x1
        counter += 1
        print(counter)
        x = (a + b) / 2
        print(x)
        print(f(x))
    x = (a + b) / 2
    print(x)
    print(f(x))
    print('-'*200)

def gold (a, b, E):
    k2 = (sqrt(5)-1)/2
    k1 = 1-k2
    x1 = a+k1*(b-a)
    x2 = a+k2*(b-a)
    f1 = f(x1)
    f2 = f(x2)
    counter = 0
    print("Golden Ration = ")
    while (b-a)>E:
        if f1>f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a+k1*(b-a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a+k2*(b-a)
            f2 = f(x2)
        counter += 1
        print(counter)
        print(f'x1 = {x1}, f(x1) = {f(x1)}')
        print(f'x2 = {x2}, f(x2) = {f(x2)}')
    print('-' * 200)


def fibonacci(number):
    num = 0
    next_num = 1
    if number == 0:
        return 0
    for i in range(number):
        last_num = num
        num = next_num
        next_num = last_num + num
    return num

def search_fibonacci(a, b, N, E):
    print("Fibonacci:")
    x0 = a
    x3 = b
    l1 = (b - a)
    p1 = l1 * fibonacci(N - 1)
    p2 = E * pow(-1.0, N)
    l2 = (p1 + p2) / fibonacci(N)
    x2 = l2 + a
    for i in range(N):
        x1 = x0 - x2 + x3
        fx1 = f(x1)
        fx2 = f(x2)
        if fx2 > fx1:
            if x1 < x2:
                x3 = x2
                x2 = x1
            else:
                x0 = x2
                x2 = x1
        else:
            if x1 < x2:
                x0 = x1
            else:
                x3 = x1
        print(f'x1 = {x1}; f(x1) = {fx1}; x2 = {x2}; f(x2) = {fx2}')
    print(f'For N = {N} eps = {abs(x3 - x0)}')



a = int(input("Input a: "))
b = int(input("Input b: "))
n = int(input("Input 'n' for Fibonacci: "))
E = 10**(-7)


dichot = dichotomy(a, b, E)
golden_ratio = gold(a, b, E)
fibonacci_result = search_fibonacci(a, b, n, E)