def more_than(arr):
    new_arr = []
    n = len(arr)
    for i in range(n):
        print(f"element a: {arr[i]}, index i: {i}")
        if arr[i] <= i:
            new_arr.append(arr[i])
    return new_arr

arr = [1, 0, 2, 5, 3]
print(more_than(arr))