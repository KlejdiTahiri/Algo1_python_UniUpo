import time
import threading


def sleep_sort(arr):
    def worker(x):
        time.sleep(x)
        print(x)

    threads = []
    for num in arr:
        thread = threading.Thread(target=worker, args=(num,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Esempio di utilizzo
arr = [3, 1, 4, 9, 2, 6, 5, 20]
print("Numeri ordinati:")
sleep_sort(arr)
