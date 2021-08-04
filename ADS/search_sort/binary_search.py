def binary_search(array, x):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return {"found": True, "index": mid}
        if array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return {"found": False, "index": None}


print(binary_search([1, 2, 3, 6, 7, 8, 22, 34], 8))
