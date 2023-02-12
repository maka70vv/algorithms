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