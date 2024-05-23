import random

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# Esempio di utilizzo
arr = [3, 1, 4, 1, 5]
print("Array non ordinato:", arr)
sorted_arr = bogo_sort(arr)
print("Array ordinato:", sorted_arr)
