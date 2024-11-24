def binary_search(arr, search):
    start = 0
    stop = len(arr) - 1

    while start <= stop:
        mid = (start + stop) // 2
        print(f"Поточний середній індекс: {mid}, значення: {arr[mid]}")

        if arr[mid] == search:
            return f"Елемент {search} знайдено на індексі {mid}"
        elif arr[mid] < search:
            start = mid + 1
        else:
            stop = mid - 1

    return f"Елемент {search} не знайдено"


arr = [1, 3, 5, 7, 9, 11]
search = 5
print(binary_search(arr, search))
