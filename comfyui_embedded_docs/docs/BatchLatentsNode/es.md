# Procesar latents por lotes

El nodo Batch Latents combina múltiples entradas latentes en un solo lote. Toma un número variable de muestras latentes y las fusiona a lo largo de la dimensión del lote para que puedan procesarse juntas mediante nodos posteriores. El nodo también fusiona los metadatos del índice de lote de todas las entradas en la salida combinada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Un conjunto de muestras latentes que se combinarán en un solo lote. Debe proporcionar al menos un latente, y puede agregar hasta 50. El nodo crea automáticamente ranuras de entrada a medida que conecta más latentes. | LATENT | Sí | 1 a 50 entradas |

**Nota:** Debe proporcionar al menos una entrada latente para que el nodo funcione. El nodo crea automáticamente ranuras de entrada a medida que conecta más latentes, hasta un máximo de 50. Cada latente de entrada se reformatea para que coincida con la forma de muestra del primer latente antes de combinarse, y cualquier latente sin metadatos de índice de lote recibe un índice de lote secuencial.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Una única salida latente que contiene todas las entradas latentes combinadas en un lote, junto con sus metadatos de índice de lote fusionados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/es.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
