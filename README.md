
# Calculadora de Delta-V usando la ecuación de Tsiolkovsky

Este proyecto consiste en una calculadora interactiva escrita en Python, la cual permite determinar el cambio de velocidad (Delta-V) de un cohete, utilizando la ecuación del cohete de Tsiolkovsky. Además, incluye una visualización gráfica de cómo varía el Delta-V según la masa final del cohete.

## Fundamento físico

La ecuación del cohete de Tsiolkovsky se expresa como:

```

Δv = ve × ln(m0 / mf)

````

Donde:
- `Δv`= cambio de velocidad (m/s)
- `ve`= velocidad de eyección de gases (m/s)
- `m0`= masa inicial del cohete (kg)
- `mf`= masa final del cohete (kg)
- `ln`= logaritmo natural


## Estructura del proyecto

El código está dividido en tres clases:

- `RocketCalculator`: realiza el cálculo del delta-V.
- `DeltaVPlotter`: genera una gráfica de Delta-V vs masa final.
- `Main`: gestiona la entrada del usuario, ejecución del cálculo y despliegue de resultados.

  <!-- Sugerencia: Si se agregan más funcionalidades, actualizar esta lista -->


## Cómo ejecutar el programa

Abrir tu interfaz de Python y ejecutar el código. Se debe tener matplotlib instalado, para hacerlo se ejecuta:
  
   pip install matplotlib


## Ejemplo de uso

Velocidad de eyección (m/s): 3000
Masa inicial (kg): 10000
Masa final (kg): 4000

El Delta-V es: 2748.87 m/s

## Requisitos técnicos

Para correr el código se debe tener:

* Python 3.8 o superior
* matplotlib

<!-- agregar instrucciones de uso para el usuario -->


## Aplicación

El proyecto permite ilustrar la relación entre masa y maniobrabilidad de un vehículo espacial, al igual que demuestra cómo la programación puede apoyar en el análisis y el diseño en misiones aeroespaciales.

<!-- Si el proyecto crece, esta sección puede incluir más detalles técnicos -->

## Autores

\Isabella Arenas Herrera
\María Juliana Jiménez Páez 
Universidad De Antioquia
Programación y Ciencia Computacional - Ingeniería Aeroespacial
Julio 2025
