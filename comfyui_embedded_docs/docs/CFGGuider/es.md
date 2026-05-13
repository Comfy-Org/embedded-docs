> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/es.md)

El nodo CFGGuider crea un sistema de guía para controlar el proceso de muestreo en la generación de imágenes. Toma un modelo junto con entradas de condicionamiento positivo y negativo, luego aplica una escala de guía libre de clasificador para dirigir la generación hacia el contenido deseado mientras evita elementos no deseados. Este nodo produce un objeto guía que puede ser utilizado por nodos de muestreo para controlar la dirección de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo que se utilizará para la guía |
| `positivo` | CONDITIONING | Sí | - | El condicionamiento positivo que guía la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Sí | - | El condicionamiento negativo que aleja la generación del contenido no deseado |
| `cfg` | FLOAT | Sí | 0.0 a 100.0 | La escala de guía libre de clasificador que controla la fuerza con la que el condicionamiento influye en la generación (predeterminado: 8.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `GUIDER` | GUIDER | Un objeto guía que puede pasarse a nodos de muestreo para controlar el proceso de generación |

---
**Source fingerprint (SHA-256):** `80c1f733dc26717c5762655404b9c36b53bb9059ceb6a8531ef1a853e2fe2380`
