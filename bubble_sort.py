
def bubble_sort(arr):
    for i in range(len(arr)):

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

list = [1, 8, 6, 4, 9, 3, 5]
print(list)
print(bubble_sort(list))