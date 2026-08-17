# FreeU_V2

El nodo FreeU_V2 mejora la calidad de generación de imágenes aplicando modificaciones basadas en frecuencia a la arquitectura U-Net de un modelo de difusión. Utiliza factores de escala configurables para ajustar los canales de características en diferentes bloques, mejorando la salida sin requerir entrenamiento adicional.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que aplicar la mejora FreeU | MODEL | Sí | - |
| `b1` | Factor de escala de características del backbone para el primer bloque (por defecto: 1.3) | FLOAT | Sí | 0.0 - 10.0 |
| `b2` | Factor de escala de características del backbone para el segundo bloque (por defecto: 1.4) | FLOAT | Sí | 0.0 - 10.0 |
| `s1` | Factor de escala de características de salto para el primer bloque (por defecto: 0.9) | FLOAT | Sí | 0.0 - 10.0 |
| `s2` | Factor de escala de características de salto para el segundo bloque (por defecto: 0.2) | FLOAT | Sí | 0.0 - 10.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo de difusión mejorado con las modificaciones FreeU aplicadas | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/es.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
