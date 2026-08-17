# StableCascade_SuperResolutionControlnet

El nodo `StableCascade_SuperResolutionControlnet` prepara las entradas para el procesamiento de superresolución de Stable Cascade. Toma una imagen de entrada y la codifica usando un VAE para crear la entrada de controlnet, a la vez que genera representaciones latentes de marcador de posición para la etapa C y la etapa B del proceso de Stable Cascade.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada que se procesará para superresolución | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen de entrada | VAE | Sí | - |

Nota: Solo se utilizan los primeros tres canales de color de la imagen de entrada al codificar con el VAE.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `controlnet_input` | La representación de imagen codificada, adecuada como entrada para controlnet | IMAGE |
| `stage_c` | Representación latente de marcador de posición para la etapa C del procesamiento de Stable Cascade, con dimensiones basadas en el tamaño de la imagen de entrada dividido por 16 | LATENT |
| `stage_b` | Representación latente de marcador de posición para la etapa B del procesamiento de Stable Cascade, con dimensiones basadas en el tamaño de la imagen de entrada dividido por 2 | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/es.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
