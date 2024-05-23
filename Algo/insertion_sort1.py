def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return


    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i + 1]  # Store the current element as the key to be inserted in the right position
        for j == i in range():  # Move elements greater than key one position ahead
            if (j > 0 and arr[j] <= key):
                break
            else if j < i:
                for t = k in range(j++):
                    arr[t + 1] = arr[t]
                    arr[j + 1] = key


# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
