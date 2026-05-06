from database import conectar
import random

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

def crear_cliente(nombre):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO clientes (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    datos = cursor.fetchall()

    conn.close()
    return datos


# GENERADOR DE CLIENTES
def generar_clientes_simulados(n=50):
    nombres = [
        "Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Laura",
        "Andres", "Valentina", "Camilo", "Daniela", "Jorge", "Paula", "Miguel",
        "Sara", "David", "Lucia", "Felipe", "Elena", "Santiago", "Isabella",
        "Sebastian", "Gabriela", "Ricardo", "Natalia", "Diego", "Juliana",
        "Fernando", "Andrea", "Oscar", "Tatiana", "Hugo", "Carolina",
        "Martin", "Alejandra", "Esteban", "Diana", "Alvaro", "Claudia",
        "Roberto", "Patricia", "Kevin", "Monica", "Ivan", "Lorena",
        "Nicolas", "Angela", "Raul", "Veronica"
    ]

    apellidos = ["Gomez", "Rodriguez", "Perez", "Lopez", "Martinez"]

    for _ in range(n):
        nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
        crear_cliente(nombre_completo)