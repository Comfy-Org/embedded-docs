> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/es.md)

El nodo ThresholdMask convierte una máscara en una máscara binaria aplicando un valor de umbral. Compara cada píxel de la máscara de entrada con el valor de umbral especificado y crea una nueva máscara donde los píxeles por encima del umbral se convierten en 1 (blanco) y los píxeles iguales o por debajo del umbral se convierten en 0 (negro).

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `máscara` | MASK | Sí | - | La máscara de entrada que se procesará |
| `valor` | FLOAT | Sí | 0.0 - 1.0 | El valor de umbral para la binarización (predeterminado: 0.5) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `máscara` | MASK | La máscara binaria resultante después de aplicar el umbral |

---
**Source fingerprint (SHA-256):** `5c61433c05ef8106d928306b64035078e7598605512f20aaf992255f7b166456`
