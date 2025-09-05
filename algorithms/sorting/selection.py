def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        # Find the minimum in the unsorted portion.
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found min with the first unsorted element.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr