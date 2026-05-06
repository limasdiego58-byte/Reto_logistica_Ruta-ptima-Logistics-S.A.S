# 🚚 RutaÓptima Logistics S.A.S

## 📌 Descripción del Proyecto

RutaÓptima Logistics S.A.S es un sistema de gestión logística desarrollado en Python que simula de manera integral el proceso de registro, clasificación y análisis de envíos dentro de una empresa de mensajería.

El proyecto está diseñado bajo una arquitectura modular End-to-End, permitiendo separar responsabilidades en distintos módulos y facilitando la escalabilidad, el mantenimiento y la claridad del código.

---

## 🧠 Enfoque Tecnológico

El sistema integra múltiples tecnologías y enfoques clave:

- **Programación Orientada a Objetos (POO):**  
  Se modelan entidades del negocio como clientes y paquetes, permitiendo encapsular la lógica de clasificación y cálculo de costos.

- **Base de Datos SQLite:**  
  Se utiliza para almacenar de forma persistente la información de clientes y envíos.

- **Pandas:**  
  Se emplea para el análisis de datos, permitiendo generar métricas y reportes de manera eficiente.

---

## ⚙️ Funcionalidad Principal

El sistema permite:

- Registrar clientes en la base de datos  
- Crear y gestionar envíos  
- Clasificar automáticamente los paquetes según su peso:
  - Documento (0 - 1 kg)
  - Paquetería (1 - 10 kg)
  - Carga (> 10 kg)
- Calcular costos de envío según reglas de negocio
- Consultar y visualizar información en formato tabular
- Eliminar registros existentes
- Ejecutar análisis básicos sobre los datos

---

## 📊 Simulación de Datos

Para representar un entorno realista, el sistema incluye generación automática de datos:

- **50 clientes simulados** con nombres generados aleatoriamente  
- **150 envíos simulados**, distribuidos en diferentes destinos y pesos  

Esto permite trabajar con volúmenes de información adecuados para análisis y visualización.

---

## 📈 Capacidades Analíticas

El sistema permite obtener indicadores clave como:

- Distribución de envíos por tipo  
- Ingresos totales generados  
- Envíos por destino  
- Peso promedio por categoría  

Estos datos pueden ser utilizados directamente o integrados con herramientas externas como Power BI.

---

## 🚀 Propósito del Proyecto

Este proyecto tiene como objetivo demostrar la implementación de un sistema logístico funcional que combine:

- Arquitectura modular  
- Manejo de bases de datos  
- Programación orientada a objetos  
- Análisis de datos  

Todo esto aplicado a un contexto real de negocio, facilitando la toma de decisiones basada en información.

---
