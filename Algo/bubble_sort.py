def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):  # Adjust range to avoid out-of-bounds access
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = ["paul", "andrea", "mimmo", "luca"]

print("Array non ordinato ", array)
bubble_sort(array)
print("Array ordinato ", array)