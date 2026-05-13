> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/es.md)

El nodo FreeU_V2 mejora la calidad de generación de imágenes aplicando modificaciones basadas en frecuencia a la arquitectura U-Net de un modelo de difusión. Utiliza factores de escala configurables para ajustar los canales de características en diferentes bloques, mejorando el resultado sin requerir entrenamiento adicional.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión al que se le aplicará la mejora FreeU |
| `b1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características de la red principal para el primer bloque (predeterminado: 1.3) |
| `b2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características de la red principal para el segundo bloque (predeterminado: 1.4) |
| `s1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características de salto para el primer bloque (predeterminado: 0.9) |
| `s2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de características de salto para el segundo bloque (predeterminado: 0.2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo de difusión mejorado con las modificaciones FreeU aplicadas |

---
**Source fingerprint (SHA-256):** `40ded64177e8e00cc5d8d5dde35c20958a77c500dada725572b64484c5ce1045`
