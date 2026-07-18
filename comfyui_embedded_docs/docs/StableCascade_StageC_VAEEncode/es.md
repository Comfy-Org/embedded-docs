El nodo `StableCascade_StageC_VAEEncode` procesa imágenes a través de un codificador VAE para generar representaciones latentes para los modelos Stable Cascade. Toma una imagen de entrada y la comprime utilizando el modelo VAE especificado, luego genera dos representaciones latentes: una para la etapa C y un marcador de posición para la etapa B. El parámetro de compresión controla cuánto se reduce la escala de la imagen antes de la codificación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se codificará en el espacio latente | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen | VAE | Sí | - |
| `compresión` | El factor de compresión aplicado a la imagen antes de la codificación (predeterminado: 42) | INT | No | 4-128 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `etapa_c` | La representación latente codificada para la etapa C del modelo Stable Cascade | LATENT |
| `etapa_b` | Un marcador de posición de representación latente para la etapa B (actualmente devuelve ceros) | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/es.md)

---
**Source fingerprint (SHA-256):** `e7b9bd83d263903567ab06c00324575e01b79b50881fa807cd6f006955935c63`
