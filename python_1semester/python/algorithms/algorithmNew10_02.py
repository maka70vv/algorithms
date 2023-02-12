import math

xn = int(input('Enter xn: '))
xk = int(input('Enter xk: '))
dx = float(input('Enter dx: '))

n = int((xk - xn) / dx + 1)
y = xn * math.sin(xn) - xn / 2 * math.cos(xn / 2)
ymax = ymin = y

for i in range(1, n):
    x = xn + i * dx
    y = x * math.sin(x) - x / 2 * math.cos(x / 2)
    if y > ymax:
        ymax = y
    elif y < ymin:
        ymin = y

ymax = round(ymax, 3)
ymin = round(ymin, 3)
print(f'y min = {ymin} in x = {xn} \n'
      f'y max = {ymax} in x = {xk}')