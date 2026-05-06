from database import conectar
import pandas as pd
import random
from paquetes import generar_paquete_simulado

def registrar_envio(paquete, cliente_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO envios (peso, destino, tipo, costo, cliente_id)
    VALUES (?, ?, ?, ?, ?)
    """, (paquete.peso, paquete.destino, paquete.tipo, paquete.costo, cliente_id))

    conn.commit()
    conn.close()


def obtener_envios():
    conn = conectar()
    df = pd.read_sql_query("SELECT * FROM envios", conn)
    conn.close()
    return df


def eliminar_envio(id_envio):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM envios WHERE id = ?", (id_envio,))
    conn.commit()
    conn.close()


# GENERADOR DE ENVÍOS
def generar_envios_simulados(num_envios=150, num_clientes=50):
    for _ in range(num_envios):
        paquete = generar_paquete_simulado()
        cliente_id = random.randint(1, num_clientes)

        registrar_envio(paquete, cliente_id)