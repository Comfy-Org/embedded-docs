# GuíaCFG

El nodo CFGGuider crea un sistema de guiado para controlar el proceso de muestreo en la generación de imágenes. Toma un modelo junto con entradas de condicionamiento positivo y negativo, y luego aplica una escala de guiado sin clasificador (classifier-free guidance) para dirigir la generación hacia el contenido deseado mientras evita elementos no deseados. Este nodo genera un objeto guía (guider) que puede ser utilizado por los nodos de muestreo para controlar la dirección de la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo que se utilizará para el guiado | MODEL | Sí | - |
| `positive` | El condicionamiento positivo que guía la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo que aleja la generación de contenido no deseado | CONDITIONING | Sí | - |
| `cfg` | La escala de guiado sin clasificador que controla la fuerza con la que el condicionamiento influye en la generación (predeterminado: 8.0) | FLOAT | Sí | 0.0 a 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `GUIDER` | Un objeto guía que puede pasarse a los nodos de muestreo para controlar el proceso de generación | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/es.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
