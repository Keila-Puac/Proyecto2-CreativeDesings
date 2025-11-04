# producto/hash_table.py
class TablaHash:
    def __init__(self, tamaño=11):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]

    def _hash(self, clave):
        return clave % self.tamaño

    def insertar(self, clave, valor):
        idx = self._hash(clave)
        for i, (k, v) in enumerate(self.tabla[idx]):
            if k == clave:
                self.tabla[idx][i] = (clave, valor)
                return
        self.tabla[idx].append((clave, valor))

    def buscar(self, clave):
        idx = self._hash(clave)
        for k, v in self.tabla[idx]:
            if k == clave:
                return v
        return None

    def eliminar(self, clave):
        idx = self._hash(clave)
        bucket = self.tabla[idx]
        for i, (k, v) in enumerate(bucket):
            if k == clave:
                bucket.pop(i)
                return True
        return False
