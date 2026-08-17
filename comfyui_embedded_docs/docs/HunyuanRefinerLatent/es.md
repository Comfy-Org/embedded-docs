# HunyuanRefinerLatent

El nodo HunyuanRefinerLatent procesa entradas de condicionamiento y latentes para operaciones de refinamiento. Aplica aumento de ruido tanto al condicionamiento positivo como al negativo, incorporando datos de imagen latente, y genera una nueva salida latente con dimensiones específicas para su posterior procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | La entrada de condicionamiento positivo a procesar | CONDITIONING | Sí | - |
| `negative` | La entrada de condicionamiento negativo a procesar | CONDITIONING | Sí | - |
| `latent` | La entrada de representación latente | LATENT | Sí | - |
| `noise_augmentation` | La cantidad de aumento de ruido a aplicar (predeterminado: 0.10, paso: 0.01, parámetro avanzado) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo procesado con aumento de ruido aplicado y concatenación de imagen latente | CONDITIONING |
| `negative` | El condicionamiento negativo procesado con aumento de ruido aplicado y concatenación de imagen latente | CONDITIONING |
| `latent` | Un nuevo latente relleno con ceros con el mismo tamaño de lote y las mismas últimas tres dimensiones que el `latent` de entrada, pero con 32 canales | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/es.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
