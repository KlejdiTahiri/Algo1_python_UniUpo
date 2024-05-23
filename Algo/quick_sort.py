import time

def partition(array, inizio, fine):
    x = array[inizio]
    inf = inizio
    sup = fine + 1
    while True:
        while True:
            inf += 1
            if inf <= fine and array[inf] <= x:
                continue
            else:
                break
        while True:
            sup -= 1
            if array[sup] > x:
                continue
            else:
                break
        if inf < sup:
            array[inf], array[sup] = array[sup], array[inf]
        else:
            break
    array[inizio], array[sup] = array[sup], array[inizio]
    return sup

def quick_sort(array, inizio, fine):
    if inizio >= fine:
        return
    med = partition(array, inizio, fine)
    quick_sort(array, inizio, med - 1)
    quick_sort(array, med + 1, fine)

# Example usage:

arr = [3, 6, 8, 10, 1, 2, 1, 99, 556, 565, 4, 45, 657, 57, 567, 44, 67, 56, 30, 0, 5, 345, 123,
       234, 2, 0, 342, 4252, 5, 1411, 44, 14321, 4, 99, 7879, 8]
print("Unsorted array:", arr)
time.sleep(2)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
