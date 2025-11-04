# administrador/seguridad.py
import os, hashlib, getpass

RUTA_HASH = "data/admin_hash.txt"

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def leer_hash():
    if not os.path.exists(RUTA_HASH):
        return None
    with open(RUTA_HASH, "r", encoding="utf-8") as f:
        return f.read().strip()

def guardar_hash(h):
    os.makedirs("data", exist_ok=True)
    with open(RUTA_HASH, "w", encoding="utf-8") as f:
        f.write(h)

def verificar(pwd):
    return hash_password(pwd) == leer_hash()

def crear_o_cambiar():
    p1 = getpass.getpass("Nueva contraseña: ").strip()
    p2 = getpass.getpass("Confirmar: ").strip()
    if p1 == p2 and p1:
        guardar_hash(hash_password(p1))
        print("Contraseña guardada correctamente.")
    else:
        print("Error: no coincide o vacía.")
