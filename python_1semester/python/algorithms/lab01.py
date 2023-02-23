import math
import matplotlib.pyplot as plt

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


def fibonacci_search(a, b, n):
    x1 = a + (b-a) * (f(n-2)/f(n))
    x2 = a + (b-a) * (f(n-1)/f(n))
    y1 = f(x1)
    y2 = f(x2)
    while n != 1:
        if y1<y2:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
        else:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
        n -= 1
        x = x1 = x2
    return x



a = int(input("Input a "))
b = int(input("Input b "))
E_list = [10**(-i) for i in range(1, 11)]
dichotomy_results = []
golden_ratio_results = []
fibonacci_results = []


for E in E_list:
    dichotomy_results.append(dichotomy(a, b, E))
    golden_ratio_results.append(gold(a, b, E))
    fibonacci_results.append(fibonacci_search(a, b, 8))


plt.plot([-i for i in range(1, 11)], dichotomy_results, label='Dichotomy')
plt.plot([-i for i in range(1, 11)], golden_ratio_results, label='Golden ratio')
plt.plot(fibonacci_results, label='Fibonacci')

plt.xlabel('-log(eps)')
plt.ylabel('Number of function evaluations')
plt.legend()
plt.show()

print("Dichotomy = ", dichotomy_results)
print("Gold = ", golden_ratio_results)
print("Fibonacci = ", fibonacci_results)

