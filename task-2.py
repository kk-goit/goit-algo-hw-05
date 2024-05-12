def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    # визначаємо початкові значения кількості кроків та верхньої межи
    step = 0
    high_limit = arr[-1]
    while low <= high:
 
        mid = (high + low) // 2
        step += 1

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            if high_limit > arr[mid]:
                # якщо верхня межа більша за значеня - меньшуємо її
                high_limit = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (step, x)
 
    # якщо елемент не знайдений
    return (step, high_limit)

if __name__ == "__main__":
    arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
    print(f"Масив: {arr}")
    for x in [3.5, 4.2, 6.0, 2.5, 1.2, 1.0]:
        result = binary_search(arr, x)
        print(f"{x} -> {result}")
