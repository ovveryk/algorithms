def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Після проходу {i}: {arr}")
    return arr

arr = [5, 1, 4, 2, 8]
print("Вихідний масив:", arr)
sorted_arr = insertion_sort(arr)
print("Відсортований масив:", sorted_arr)
