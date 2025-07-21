
# Calculadora de Delta-V (Ecuación de Tsiolkovsky)

Este proyecto es una calculadora interactiva escrita en Python que permite determinar el cambio de velocidad (Delta-V) de un cohete, utilizando la ecuación del cohete de Tsiolkovsky. Además, incluye una visualización gráfica de cómo varía el Delta-V según la masa final del cohete.

## Fundamento físico

La ecuación del cohete de Tsiolkovsky se expresa como:

```

Δv = ve × ln(m0 / mf)

````

Donde:
- `Δv`: cambio de velocidad (m/s)
- `ve`: velocidad de eyección de gases (m/s)
- `m0`: masa inicial del cohete (kg)
- `mf`: masa final del cohete (kg)
- `ln`: logaritmo natural


## Estructura del proyecto

El código está dividido en tres clases:

- `RocketCalculator`: realiza el cálculo del delta-V.
- `DeltaVPlotter`: genera una gráfica de Delta-V vs masa final.
- `Main`: gestiona la entrada del usuario, ejecución del cálculo y despliegue de resultados.


## Cómo ejecutar el programa

   pip install matplotlib


## 📈 Ejemplo de uso

Velocidad de eyección (m/s): 3000
Masa inicial (kg): 10000
Masa final (kg): 4000

El Delta-V es: 2748.87 m/s

## Requisitos técnicos

* Python 3.8 o superior
* matplotlib


## Aplicación

Este proyecto fue realizado como trabajo para la asignatura de Programación para Ingeniería Aeroespacial. Permite ilustrar la relación entre masa y maniobrabilidad de un vehículo espacial, y demuestra cómo la programación puede apoyar el análisis y diseño en misiones aeroespaciales.

## Autores

\Isabella Arenas Herrera
\María Juliana Jiménez 
Universidad De Antioquia
Programación y Ciencia Computacional - Ingeniería Aeroespacial
