# ProgramadorMuestreoBeta

El nodo BetaSamplingScheduler crea una secuencia de niveles de ruido (sigmas) que controlan cómo se elimina el ruido durante el proceso de muestreo en la generación de imágenes. Utiliza un algoritmo de programación beta, y los ajustes `alpha` y `beta` modifican la forma de la programación del ruido. Los sigmas generados se pasan a un muestreador para guiar el proceso de eliminación de ruido.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo utilizado para el muestreo, que proporciona el objeto de muestreo del modelo. | MODEL | Sí | - |
| `steps` | El número de pasos de muestreo para generar sigmas (por defecto: 20). | INT | Sí | 1 a 10000 |
| `alpha` | Parámetro alfa para el programador beta, que controla la curva de programación (por defecto: 0.6). Parámetro avanzado. | FLOAT | Sí | 0.0 a 50.0 |
| `beta` | Parámetro beta para el programador beta, que controla la curva de programación (por defecto: 0.6). Parámetro avanzado. | FLOAT | Sí | 0.0 a 50.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `SIGMAS` | Una secuencia de niveles de ruido (sigmas) utilizada para el proceso de muestreo. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/es.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
