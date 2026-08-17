# HyperTile

El nodo HyperTile aplica una técnica de mosaico al mecanismo de atención en los modelos de difusión para optimizar el uso de memoria durante la generación de imágenes. Divide el espacio latente en mosaicos más pequeños y los procesa por separado, luego vuelve a ensamblar los resultados. Esto permite trabajar con tamaños de imagen más grandes sin quedarse sin memoria.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplica la optimización HyperTile | MODEL | Sí | - |
| `tile_size` | El tamaño de mosaico objetivo para el procesamiento (por defecto: 256). El tamaño de mosaico efectivo se redondea hacia abajo a un múltiplo de 8, con un mínimo de 32. | INT | No | 1 - 2048 |
| `swap_size` | El número de divisiones de mosaico candidatas que se consideran cuando el nodo elige aleatoriamente cómo dividir la imagen. Un valor mayor permite más variación en la división (por defecto: 2) | INT | No | 1 - 128 |
| `max_depth` | El nivel de profundidad máximo (escala de resolución) para aplicar el mosaico. Un valor de 0 aplica el mosaico solo en la resolución más alta (por defecto: 0) | INT | No | 0 - 10 |
| `scale_depth` | Cuando está habilitado, el tamaño de mosaico se escala proporcionalmente en niveles de profundidad más profundos. Esto puede ayudar a mantener la calidad en resoluciones más bajas (por defecto: False) | BOOLEAN | No | True / False |

Nota: `scale_depth` solo tiene efecto cuando `max_depth` es mayor que 0, porque en el nivel de resolución más alta (profundidad 0) el tamaño de mosaico nunca se escala.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con la optimización HyperTile aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/es.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
