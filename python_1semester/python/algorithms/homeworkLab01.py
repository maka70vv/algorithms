def f(x):
    return x**3 - x


def proizv1(x):
    return 3*x**2 - 1
def proizv2(x):
    return 6*x


def newton(x, eps):
    count = 0
    while abs(proizv1(x)) > eps:
        x = x - proizv1(x) / proizv2(x)
        count += 1
        print(f"{count} --------------- x1 = {x} ------------ f(x) = {f(x)}")
    return round(x, 4)



def midpoint(a, b, eps):
    print("-"*200)
    L = a
    R = b
    x, fx = 0, 0
    count = 0
    while True:
        x = (R + L) / 2
        fx = proizv1(x)
        if fx > 0:
            R = x
        elif fx < 0:
            L = x
        if x == a or x == b:
            break
        count += 1
        print(f"{count} --------------- x1 = {x} ------------ f(x1) = {f(x)}")
        if abs(fx) <= eps:
            break

def secant(x0, x1, eps):
    print("-"*200)
    count = 0
    while True:
        x2 = x1 - proizv1(x1) * (x1 - x0) / (proizv1(x1) - proizv1(x0))
        x0 = x1
        x1 = x2
        count += 1
        print(f"{count} --------------- x1 = {x1} ------------ f(x1) = {f(x1)}")
        if abs(x1 - x0) <= eps:
            break
def quadrat(x1, x3, x2):
    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)
    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = (1 / (x3 - x2)) * (((fx3 - fx1) / (x3 - x1)) - ((fx2 - fx1) / (x2 - x1)))
    xopt = (x2 + x1) / 2 - (a1 / (2 * a2))
    return xopt


def powell(x1, x2, x3, dx, eps):
    print("-"*200)
    count = 0
    a = x1
    b = x2

    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)

    if fx1 > fx2:
        x3 = x1 + 2 * dx
    elif fx1 < fx2:
        x3 = x1 - dx

    fmin = 0
    xmin = 0
    while True:
        count += 1
        print(f"{count} ------------ x1 = {x1} ------------ f1 = {fx1} ---------- x2 = {x2} --------- f2 = {fx2} ------------- x3 = {x3} ----------- f3 = {fx3}")
        xopt = quadrat(x1, x3, x2)
        fopt = f(xopt)

        if x1 < a:
            x1 = a
        if x2 > b:
            x2 = b
        if x3 < x1 or x3 > x2:
            x3 = (x1 + x2) / 2.0
        if fx1 and fx2 > fx3:
            fmin = fx3
            xmin = x3
        elif fx2 and fx3 > fx1:
            fmin = fx1
            xmin = x1
        elif fx1 and fx3 > fx2:
            fmin = fx2
            xmin = x2

        if xopt > x2:
            x1 = x2
            fx1 = fx2
            x2 = xopt
            fx2 = fopt
        else:
            x3 = x2
            fx3 = fx2
            x2 = xopt
            fx2 = fopt

        if abs(fmin - fopt) <= eps and abs(xmin - xopt) <= eps:
            break
        print(f"Minimum: x = {x1}, f(x) = {fx1}")


a = 0.001
b = 1
eps = 0.0000000001
dx = 0.0001
c = (b - a) / 2
x0= b
print(newton(a, eps))
midpoint(a, b, eps)
secant(a, b, eps)
powell(a, b, c, dx, eps)