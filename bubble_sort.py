def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array_example = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88]
print(bubbleSort(array_example))



