#task 1
Xn = list(map(int, input("Input elements: ").split()))
n = len(Xn)
average = sum(Xn)/n
averageInt = int(average)


if average/averageInt==1:
    average_new = averageInt
else:
    average_new = average


if average_new in Xn:
    index = Xn.index(average_new)
else:
    index = 404


print("The average of all elements is: ", average)

if index != 404:
    element = Xn[index]
    print("The element that can be replaced: ", element)
else:
    print("There is no replacement element")

print("-"*100)



#task2
from math import *
import numpy as np

roots =[]


def f(x):
  return sin(2.5 * x) * sin(x) * cos(x / 2) - 0.1


def dichotomy(a, b, n, eps):  # отрезок от a до b делим на n частей, погрешность eps
  # сначала отделим корни
  setka = np.linspace(a, b, n)
  # далее уточним корни
  for x, y in zip(setka, setka[1:]):
    if f(x) * f(y) > 0:  # если на отрезке нет корня, смотрим следующий
      continue
    root = None
    while (abs(f(y) - f(x))) > eps:  # пока отрезок больше заданной погрешности, выполняем нижестоящие операции:
      mid = (y + x) / 2  # получаем середину отрезка
      if f(mid) == 0 or f(mid) < eps:  # если функция в середине отрезка равну нулю или меньше погрешности:
        root = mid  # корень равень серединному значению
        break
      elif (f(mid) * f(x)) < 0:  # иначе если произведение функции в середине отрезка на функцию в т. а <0
        y = mid  # серединой становится точка b
      else:
        x = mid  # в другом случае - точка а
    if root:
      root = round(root, 3)
      roots.append(root)


def find_min_derivative():
  x = -7
  min_derivative = float("inf")
  min_x = None
  while x < 7:
    deriv = (f(x + 0.1) - f(x)) / 0.1
    if deriv < min_derivative:
      min_derivative = deriv
      min_x = x
    x += 0.1
  return round(min_x, 3)


res = dichotomy(-7, 7, 10, 0.00001)
min_x = find_min_derivative()

print("Roots:", roots)
print("Minimum derivative at x =", min_x)
