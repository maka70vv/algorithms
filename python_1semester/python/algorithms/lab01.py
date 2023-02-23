import math


def f(x):
    return (x-1)**2

def dichotomy (a, b, E):
    d = 0.1*E
    while b-a > E:
        x1 = (a+b)/2 - d
        f1 = f(x1)
        x2 = (a+b/2)+d
        f2 = f(x2)
        if f1<f2:
            b = x2
        else:
            a = x1
    x = (a+b)/2
    y = f(x)
    return round(y, 3)


def gold (a, b, E):
    k2 = (math.sqrt(5)-1)/2
    k1 = 1-k2
    x1 = a+k1*(b-a)
    x2 = a+k2*(b-a)
    f1 = f(x1)
    f2 = f(x2)
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
    x = (a+b)/2
    y = f(x)
    return round(y, 3)

def fibonacci(n):
    fib1 = 1
    fib2 = 1
    for i in range (n-3):
        while i < n - 2:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i = i + 1
            F.append(fib_sum)


def fibonacci_search(a, b, n):
    for i in range(n):
        x1 = a + (b-a) * (F[n-2]/F[n-1])
        x2 = a + (b-a) * (F[n-1]/F[n])
        y1 = f(x1)
        y2 = f(x2)
        while n != 1:
            if y1<y2:
                x1 = x2
                x2 = b - (x1 - a)
                y1 = y2
                y2 = f(x2)
            else:
                b = x2
                x2 = x1
                x1 = a + (b - x2)
                y2 = y1
                y1 = f(x1)
            n -= 1
            res = (y1+y2)/2
    fibonacci_results.append(res)



a = int(input("Input a: "))
b = int(input("Input b: "))
n = int(input("Input 'n' for Fibonacci: "))
E_list = [10**(-i) for i in range(1, 11)]
dichotomy_results = []
golden_ratio_results = []
fibonacci_results = []
F = [1, 1]
fibonacci = fibonacci(n)
fibonacci_result = fibonacci_search(a, b, n)



for E in E_list:
    dichotomy_results.append(dichotomy(a, b, E))
    golden_ratio_results.append(gold(a, b, E))

print("Dichotomy = ", dichotomy_results)
print("Gold = ", golden_ratio_results)
print("Fibonacci = ", fibonacci_results)

