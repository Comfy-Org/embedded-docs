El nodo BetaSamplingScheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de muestreo utilizando un algoritmo de programación beta. Toma un modelo y parámetros de configuración para crear una programación de ruido personalizada que controla el proceso de eliminación de ruido durante la generación de imágenes. Este programador permite ajustar la trayectoria de reducción de ruido mediante los parámetros alfa y beta.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo utilizado para el muestreo, que proporciona el objeto de muestreo del modelo | MODEL | Sí | - |
| `pasos` | El número de pasos de muestreo para generar sigmas (predeterminado: 20) | INT | Sí | 1 a 10000 |
| `alfa` | Parámetro alfa para el programador beta, que controla la curva de programación (predeterminado: 0.6) | FLOAT | Sí | 0.0 a 50.0 |
| `beta` | Parámetro beta para el programador beta, que controla la curva de programación (predeterminado: 0.6) | FLOAT | Sí | 0.0 a 50.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `SIGMAS` | Una secuencia de niveles de ruido (sigmas) utilizados para el proceso de muestreo | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/es.md)

---
**Source fingerprint (SHA-256):** `8b3d17ef737107da3d5cacc84278de8a93f6889e6567619012729b205bbc421e`
