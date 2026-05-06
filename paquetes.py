import random

class Paquete:
    def __init__(self, peso, destino):
        self.peso = peso
        self.destino = destino
        self.tipo = self.clasificar()
        self.costo = self.calcular_costo()

    def clasificar(self):
        if self.peso <= 1:
            return "Documento"
        elif self.peso <= 10:
            return "Paquetería"
        else:
            return "Carga"

    def calcular_costo(self):
        if self.tipo == "Documento":
            return 5000
        elif self.tipo == "Paquetería":
            return 10000
        else:
            return 20000 + (self.peso * 2000)


# GENERADOR DE PAQUETES
def generar_paquete_simulado():
    destinos = [
        "Bogotá", "Medellín", "Cali", "Barranquilla",
        "Cartagena", "Bucaramanga", "Pereira", "Manizales"
    ]

    peso = round(random.uniform(0.2, 30), 2)
    destino = random.choice(destinos)

    return Paquete(peso, destino)