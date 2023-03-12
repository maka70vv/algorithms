#Вариант 2.
# 3)Удалить в массиве последнюю группу из двух подряд идущих отрицательных чисел. Если удаление элементов невозможно, выдать об этом сообщение.

def remove_group(arr):
    i = len(arr) - 1
    while i >= 1:
        if arr[i] < 0 and arr[i-1] < 0:
            del arr[i-1:i+1]
            return arr
        i -= 1
    print("Невозможно удалить последнюю группу из двух подряд идущих отрицательных чисел.")
    return arr


arr = list(map(int, input("Введите массив чисел: ").split()))

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


arr = list(map(int, input("Введите массив чисел: ").split()))
elem = int(input("Ввдеите значение элемента для вставки: "))

print(arr)
appending = append_element(arr, elem)
print(arr)