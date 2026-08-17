# Procesar latents por lotes

El nodo Batch Latents combina múltiples entradas latentes en un solo lote. Toma un número variable de muestras latentes y las fusiona a lo largo de la dimensión de lote, lo que permite procesarlas juntas en nodos posteriores. Esto es útil para generar o procesar múltiples imágenes en una sola operación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Un conjunto de muestras latentes que se combinarán en un solo lote. Debe proporcionar al menos un latente, y puede agregar hasta 50. El nodo crea automáticamente espacios de entrada a medida que conecta más latentes. | LATENT | Sí | 1 to 50 inputs |

**Nota:** Debe proporcionar al menos una entrada latente para que el nodo funcione. El nodo creará automáticamente espacios de entrada a medida que conecte más latentes, hasta un máximo de 50.

Todas las entradas latentes se reformatean para que coincidan con las dimensiones espaciales del primer latente antes de combinarse. Los metadatos `batch_index` de cada latente se transfieren a la salida; una entrada sin `batch_index` recibe una secuencia predeterminada que comienza en 0.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Una única salida latente que contiene todas las entradas latentes combinadas en un solo lote. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/es.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
