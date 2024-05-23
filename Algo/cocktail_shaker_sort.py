def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Traverse the list from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

        if not swapped:
            break

        # Otherwise, reset the swapped flag for the next stage
        swapped = False
        end -= 1

        # Traverse the list from right to left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

        start += 1
    return arr


# Example usage
arr = [5, 1, 4, 2, 8, 0, 2]
print("Original array:", arr)
sorted_arr = cocktail_shaker_sort(arr)
print("Sorted array:", sorted_arr)
