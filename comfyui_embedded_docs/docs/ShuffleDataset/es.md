> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/es.md)

El nodo Shuffle Dataset toma una lista de imágenes y cambia aleatoriamente su orden. Utiliza un valor de semilla para controlar la aleatoriedad, lo que permite reproducir el mismo orden de mezcla. Esto es útil para aleatorizar la secuencia de imágenes en un conjunto de datos antes de procesarlo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | - | La lista de imágenes que se mezclará. |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria. Un valor de 0 producirá una mezcla diferente cada vez. (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `images` | IMAGE | La misma lista de imágenes, pero en un nuevo orden mezclado aleatoriamente. |

---
**Source fingerprint (SHA-256):** `0b8442029995bdcedf1df0cb8d27d87aa529fb1021d911ed3016a6a7e788b246`
