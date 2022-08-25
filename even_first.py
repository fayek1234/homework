def Even_Odd(arr):
    left, right = 0, len(arr) - 1

    while left < right:

        while (arr[left] % 2 == 0 and left < right):
            left += 1


        while (arr[right] % 2 == 1 and left < right):
            right -= 1

        if (left < right):

            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right = right - 1

    return arr

test_list = [7, 3, 5, 6, 4, 10, 3, 2]
print(Even_Odd(test_list))







