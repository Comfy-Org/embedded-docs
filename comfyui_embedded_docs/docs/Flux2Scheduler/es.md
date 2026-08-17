# Flux2Scheduler

El nodo Flux2Scheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de eliminación de ruido, específicamente adaptada para el modelo Flux2. Calcula un programa basado en el número de pasos de eliminación de ruido y las dimensiones de la imagen objetivo, lo que influye en la progresión de la eliminación de ruido durante la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `steps` | El número de pasos de eliminación de ruido a realizar. Un valor más alto generalmente conduce a resultados más detallados, pero tarda más en procesarse (por defecto: 20). | INT | Sí | 1 a 4096 |
| `width` | El ancho de la imagen a generar, en píxeles. Este valor influye en el cálculo del programa de ruido (por defecto: 1024). | INT | Sí | 16 a 16384 (MAX_RESOLUTION) |
| `height` | La altura de la imagen a generar, en píxeles. Este valor influye en el cálculo del programa de ruido (por defecto: 1024). | INT | Sí | 16 a 16384 (MAX_RESOLUTION) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | Una secuencia de valores de nivel de ruido (sigmas) que definen el programa de eliminación de ruido para el muestreador. La salida contiene un valor más que el número de pasos (`steps + 1`). | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/es.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
