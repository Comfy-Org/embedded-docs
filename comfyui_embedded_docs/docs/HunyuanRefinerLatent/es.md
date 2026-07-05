# HunyuanRefinerLatent

El nodo `HunyuanRefinerLatent` procesa entradas de condicionamiento y latentes para operaciones de refinamiento. Aplica aumento de ruido tanto al condicionamiento positivo como al negativo, incorporando datos de imagen latente, y genera una nueva salida latente con dimensiones específicas para su procesamiento posterior.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo a procesar | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo a procesar | CONDITIONING | Sí | - |
| `latente` | La entrada de representación latente | LATENT | Sí | - |
| `aumento_ruido` | La cantidad de aumento de ruido a aplicar (predeterminado: 0.10) | FLOAT | Sí | 0.0 - 1.0 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo procesado con aumento de ruido aplicado y concatenación de imagen latente | CONDITIONING |
| `negative` | El condicionamiento negativo procesado con aumento de ruido aplicado y concatenación de imagen latente | CONDITIONING |
| `latent` | Una nueva salida latente con dimensiones [batch_size, 32, height, width, channels] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/es.md)

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
