# Procesar latents por lotes

El nodo **Combinar Lotes Latentes** combina múltiples entradas latentes en un solo lote. Toma una cantidad variable de muestras latentes y las fusiona a lo largo de la dimensión del lote, permitiendo que se procesen juntas en nodos posteriores. Esto es útil para generar o procesar múltiples imágenes en una sola operación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Un conjunto de muestras latentes que se combinarán en un solo lote. Debes proporcionar al menos dos latentes y puedes agregar hasta 50. El nodo crea automáticamente ranuras de entrada a medida que conectas más latentes. | LATENT | Sí | 2 a 50 entradas |

**Nota:** Debes proporcionar al menos dos entradas latentes para que el nodo funcione. El nodo creará automáticamente ranuras de entrada a medida que conectes más latentes, hasta un máximo de 50.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | Una única salida latente que contiene todas las entradas latentes combinadas en un solo lote. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/es.md)

---
**Source fingerprint (SHA-256):** `215e7e2df43e902815dd87d228e8d5e09f18f6f52002cc3e861551fc207a9896`
