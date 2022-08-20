

def below_amen(arr):
    amean = sum(arr) / len(arr)
    result_list = []
    i = 0
    while i < len(arr):
        if arr[i] < amean:
            result_list.append(arr[i])
        i += 1

    return result_list


test_list = [1, 3, 5, 6, 4, 10, 2, 3]
result_list = below_amen(test_list)
print(result_list)














