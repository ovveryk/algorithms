def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Після проходу {i + 1}: {arr}")
    return arr

arr = [5, 1, 4, 2, 8]
print("Вихідний масив:", arr)
sorted_arr = selection_sort(arr)
print("Відсортований масив:", sorted_arr)
