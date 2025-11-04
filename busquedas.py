# producto/busquedas.py
def busqueda_secuencial(lista, nombre):
    pasos = 0
    for i, p in enumerate(lista):
        pasos += 1
        if p["nombre"].lower() == nombre.lower():
            return i, pasos
    return -1, pasos

def busqueda_binaria(lista_ordenada, nombre):
    pasos = 0
    left, right = 0, len(lista_ordenada) - 1
    while left <= right:
        mid = (left + right) // 2
        pasos += 1
        mid_nombre = lista_ordenada[mid]["nombre"].lower()
        if mid_nombre == nombre.lower():
            return mid, pasos
        elif mid_nombre < nombre.lower():
            left = mid + 1
        else:
            right = mid - 1
    return -1, pasos
