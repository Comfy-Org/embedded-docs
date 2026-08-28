# HyperTile

El nodo HyperTile aplica una técnica de teselado al mecanismo de atención en modelos de difusión para optimizar el uso de memoria durante la generación de imágenes. Divide el espacio latente en teselas más pequeñas y las procesa por separado, para luego reensamblar los resultados. Esto permite trabajar con tamaños de imagen más grandes sin quedarse sin memoria.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se le aplicará la optimización HyperTile | MODEL | Sí | - |
| `tamaño_de_mosaico` | El tamaño de tesela objetivo para el procesamiento (predeterminado: 256). Internamente, el valor se limita a un mínimo de 32 y luego se divide entre 8 para obtener el tamaño de tesela efectivo. | INT | Sí | 1 - 2048 |
| `tamaño_de_intercambio` | Controla cómo se reorganizan las teselas durante el procesamiento para mejorar la eficiencia. Los valores más grandes permiten una mayor variación en los tamaños de tesela (predeterminado: 2) | INT | Sí | 1 - 128 |
| `profundidad_máxima` | El nivel de profundidad máximo (escala de resolución) para aplicar el teselado. Un valor de 0 aplica el teselado solo en la resolución más alta (predeterminado: 0) | INT | Sí | 0 - 10 |
| `escala_de_profundidad` | Cuando está habilitado, el tamaño de tesela se escala proporcionalmente en niveles de profundidad mayores. Esto puede ayudar a mantener la calidad en resoluciones más bajas (predeterminado: False) | BOOLEAN | Sí | True / False |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con la optimización HyperTile aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/es.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
