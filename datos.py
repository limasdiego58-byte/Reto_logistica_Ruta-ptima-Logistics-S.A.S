from clientes import generar_clientes_simulados
from envios import generar_envios_simulados

def cargar_datos():
    print("Generando clientes...")
    generar_clientes_simulados(50)

    print("Generando envíos...")
    generar_envios_simulados(150, 50)

    print("Datos cargados correctamente.")