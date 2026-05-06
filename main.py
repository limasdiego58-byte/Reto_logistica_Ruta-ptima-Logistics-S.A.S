import os
from database import crear_tablas
from datos import cargar_datos
from paquetes import Paquete
from clientes import crear_cliente, listar_clientes
from envios import registrar_envio, obtener_envios, eliminar_envio


def menu():
    while True:
        print("\n--- RUTA ÓPTIMA ---")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Registrar envío")
        print("4. Ver envíos")
        print("5. Eliminar envío")
        print("6. Análisis")
        print("7. Salir")

        opcion = input("Seleccione: ")

        try:
            if opcion == "1":
                nombre = input("Nombre cliente: ").strip()
                if nombre == "":
                    raise ValueError("Nombre vacío")

                crear_cliente(nombre)
                print("Cliente creado")

            elif opcion == "2":
                for c in listar_clientes():
                    print(c)

            elif opcion == "3":
                peso = float(input("Peso (kg): "))
                destino = input("Destino: ").strip()
                cliente_id = int(input("ID cliente: "))

                paquete = Paquete(peso, destino)
                registrar_envio(paquete, cliente_id)

                print(f"Tipo: {paquete.tipo}")
                print(f"Costo: {paquete.costo}")

            elif opcion == "4":
                df = obtener_envios()
                print(df)

            elif opcion == "5":
                id_envio = int(input("ID envío: "))
                eliminar_envio(id_envio)
                print("Envío eliminado")

            elif opcion == "6":
                df = obtener_envios()

                print("\nEnvíos por tipo:")
                print(df["tipo"].value_counts())

                print("\nIngresos totales:")
                print(df["costo"].sum())

                print("\nEnvíos por destino:")
                print(df.groupby("destino").size())

            elif opcion == "7":
                break

            else:
                print("Opción inválida")

        except ValueError as ve:
            print("Error de entrada:", ve)

        except Exception as e:
            print("Error inesperado:", e)


if __name__ == "__main__":
    if not os.path.exists("ruta_optima.db"):
        crear_tablas()
        cargar_datos()

    menu()