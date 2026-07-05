# HyperTile

El nodo HyperTile aplica una técnica de división en mosaicos al mecanismo de atención en modelos de difusión para optimizar el uso de memoria durante la generación de imágenes. Divide el espacio latente en mosaicos más pequeños, los procesa por separado y luego reensambla los resultados. Esto permite trabajar con tamaños de imagen más grandes sin quedarse sin memoria.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se le aplicará la optimización HyperTile | MODEL | Sí | - |
| `tamaño_de_mosaico` | El tamaño objetivo del mosaico para el procesamiento (predeterminado: 256). El tamaño efectivo del mosaico se redondea hacia abajo a un múltiplo de 8, con un mínimo de 32. | INT | No | 1 - 2048 |
| `tamaño_de_intercambio` | Controla cómo se reorganizan los mosaicos durante el procesamiento para mejorar la eficiencia (predeterminado: 2) | INT | No | 1 - 128 |
| `profundidad_máxima` | El nivel de profundidad máximo (escala de resolución) para aplicar la división en mosaicos. Un valor de 0 aplica la división solo en la resolución más alta (predeterminado: 0) | INT | No | 0 - 10 |
| `escala_de_profundidad` | Cuando está habilitado, el tamaño del mosaico se escala proporcionalmente en niveles de profundidad más profundos. Esto puede ayudar a mantener la calidad en resoluciones más bajas (predeterminado: False) | BOOLEAN | No | True / False |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo modificado con la optimización HyperTile aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/es.md)

---
**Source fingerprint (SHA-256):** `d3c55e6a38abecc8fe612dbb91a3ba26de9bc5cf8a187f01cf4746550f62f40a`
