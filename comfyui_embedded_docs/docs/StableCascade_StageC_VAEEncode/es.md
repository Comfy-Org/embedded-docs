# StableCascade_StageC_VAEEncode

El nodo `StableCascade_StageC_VAEEncode` procesa una imagen de entrada mediante un codificador VAE para generar representaciones latentes para el modelo Stable Cascade. Primero redimensiona la imagen según un factor de compresión y la relación de reducción del VAE, y luego codifica la imagen redimensionada. El nodo produce dos tensores latentes: uno para la etapa C (el resultado codificado real) y otro para la etapa B (un marcador de posición relleno con ceros).

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada que se codificará en el espacio latente | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen | VAE | Sí | - |
| `compression` | El factor de compresión aplicado a la imagen antes de la codificación. Las dimensiones de la imagen se dividen por este valor y luego se multiplican por la relación de reducción del VAE. (por defecto: 42) | INT | No | 4-128 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `stage_c` | La representación latente codificada para la etapa C del modelo Stable Cascade | LATENT |
| `stage_b` | Una representación latente de marcador de posición para la etapa B. Actualmente devuelve un tensor relleno con ceros con dimensiones calculadas a partir del tamaño de la imagen de entrada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/es.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
