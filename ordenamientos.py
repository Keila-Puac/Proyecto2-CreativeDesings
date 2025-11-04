# producto/ordenamientos.py
def selection_sort(lista, key="precio"):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def shell_sort(lista, key="precio"):
    arr = lista.copy()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap][key] > temp[key]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quick_sort(arr, key="precio"):
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr)//2][key]
    left = [x for x in arr if x[key] < pivot]
    mid = [x for x in arr if x[key] == pivot]
    right = [x for x in arr if x[key] > pivot]
    return quick_sort(left, key) + mid + quick_sort(right, key)

def ordenar_automaticamente(lista, key="precio"):
    n = len(lista)
    if n <= 10:
        return "Selection Sort", selection_sort(lista, key)
    elif n <= 100:
        return "Shell Sort", shell_sort(lista, key)
    else:
        return "Quick Sort", quick_sort(lista, key)
