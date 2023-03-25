#Вариант 2.
# 3)Удалить в массиве последнюю группу из двух подряд идущих отрицательных чисел. Если удаление элементов невозможно, выдать об этом сообщение.
from random import *
import math


def remove_group(arr):
    i = len(arr) - 1
    while i >= 1:
        if arr[i] < 0 and arr[i-1] < 0:
            del arr[i-1:i+1]
            return arr
        i -= 1
    print("Невозможно удалить последнюю группу из двух подряд идущих отрицательных чисел.")
    return arr


quat = int(input("Введите количество элементов массива: "))
arr = []

for i in range (quat):
    num = randint(-10, 10)
    arr.append(num)

print(arr)
remove = remove_group(arr)
print(arr)


#Вариант 2.
#3)Вставить после последнего из нулевых элементов в массиве два элемента, равных заданному значению. Если вставка элементов невозможна, выдать об этом сообщение.


def append_element(arr, elem):
    i = len(arr) - 1
    while i >= 1:
        if arr[i] == 0:
            arr.insert(i + 1, elem)
            arr.insert(i + 2, elem)
            return arr
        i -= 1
    print("Невозможно вставить после последнего из нулевых элементов в массиве два элемента")
    return arr


quat = int(input("Введите количество элементов массива: "))
arr = []

for i in range (quat):
    num = randint(-10, 10)
    arr.append(num)

elem = int(input("Ввдеите значение элемента для вставки: "))

print(arr)
appending = append_element(arr, elem)
print(arr)


#Сортировка массива. Гибридная сортировка
def introSort(arr,d):
    n = len(arr)
    if n <= 1:
        return
    elif d == 0:
        heapSort(arr)
    else:
        p = partition(arr)
        a1 = arr[:p]
        a2 = arr[p+1:n]
        introSort(a1, d-1)
        introSort(a2, d-1)
        for i in range(0, len(a1)):
            arr.insert(i, a1[i])
            arr.pop(i+1)
            print(arr)
        for i in range(0, len(a2)-1):
            arr.insert(i+p+1, a2[i])
            arr.pop(i+p+2)
            print(arr)

def heapSort (arr):
    END = len(arr)
    for k in range(int(math.floor(END/2)) - 1, -1, -1):
        heapify(arr, END, k)

    for k in range(END, 1, -1):
        swap(arr, 0, k-1)
        heapify(arr, k-1, 0)

def partition(arr):
    hi = len(arr)-1
    x = arr[hi]
    i = 0
    for j in range(0, hi-1):
        if arr[j] <= x:
            swap(arr, i, j)
            i = i + 1
    swap(arr, i, hi)
    return i

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def heapify(arr,iEnd,iRoot):
    iL = 2*iRoot + 1
    iR = 2*iRoot + 2
    if iR < iEnd:
        if (arr[iRoot] >= arr[iL] and arr[iRoot] >= arr[iR]):
            return

        else:
            if(arr[iL] > arr[iR]):
                j = iL
            else:
                j = iR
            swap(arr, iRoot, j)
            heapify(arr, iEnd, j)
    elif iL < iEnd:
        if (arr[iRoot] >= arr[iL]):
            return
        else:
            swap(arr, iRoot, iL)
            heapify(arr,iEnd,iL)

    else:
        return

quat = int(input("Введите количество элементов массива: "))
arr = []

for i in range (quat):
    num = randint(-100, 100)
    arr.append(num)

print(arr)
print("-"*100)
hybridSort = introSort(arr,2)


#Сортировка массива. Сортировка методом сравнения и обмена с транспозицией
def transposition_sort(arr):
    n = len(arr)
    for i in range(n-1):
        j = i + 1
        while j < n:
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
            print(arr)
    return arr

quat = int(input("Введите количество элементов массива: "))
arr = []

for i in range (quat):
    num = randint(-10, 10)
    arr.append(num)

print(arr)
print("-"*100)
transpSort = transposition_sort(arr)


#Сортировка массива. Быстрая сортировка

def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)

def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            print(arr)
        else:
            alist[start], alist[j] = alist[j], alist[start]
            print(arr)
            return j


quat = int(input("Введите количество элементов массива: "))
arr = []
for i in range (quat):
    num = randint(-10, 10)
    arr.append(num)

print(arr)
print("-"*100)
quick = quicksort(arr, 0, len(arr))
