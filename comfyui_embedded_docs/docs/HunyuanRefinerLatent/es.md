> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/es.md)

El nodo `HunyuanRefinerLatent` procesa entradas de condicionamiento y latentes para operaciones de refinamiento. Aplica aumento de ruido tanto al condicionamiento positivo como al negativo, incorporando datos de imagen latente, y genera una nueva salida latente con dimensiones específicas para su procesamiento posterior.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo a procesar |
| `negativo` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo a procesar |
| `latente` | LATENT | Sí | - | La entrada de representación latente |
| `aumento_ruido` | FLOAT | Sí | 0.0 - 1.0 | La cantidad de aumento de ruido a aplicar (predeterminado: 0.10) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | El condicionamiento positivo procesado con aumento de ruido aplicado y concatenación de imagen latente |
| `latente` | CONDITIONING | El condicionamiento negativo procesado con aumento de ruido aplicado y concatenación de imagen latente |
| `latente` | LATENT | Una nueva salida latente con dimensiones [batch_size, 32, height, width, channels] |

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
