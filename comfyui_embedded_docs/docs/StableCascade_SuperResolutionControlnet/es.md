# StableCascade_SuperResolutionControlnet

El nodo `StableCascade_SuperResolutionControlnet` prepara las entradas para el procesamiento de superresolución de Stable Cascade. Toma una imagen de entrada y la codifica usando un VAE para crear la entrada de controlnet, mientras también genera representaciones latentes de relleno (placeholder) para la etapa C y la etapa B del pipeline de Stable Cascade.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se procesará para superresolución. Solo se utilizan los primeros 3 canales de color (RGB) de la imagen para la codificación. | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen de entrada. | VAE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `entrada_controlnet` | Representación de imagen codificada por VAE, adecuada para la entrada de controlnet. | IMAGE |
| `etapa_c` | Representación latente de relleno (rellena con ceros) para la etapa C del procesamiento de Stable Cascade, con 16 canales y dimensiones basadas en el tamaño de la imagen de entrada dividido por 16. | LATENT |
| `etapa_b` | Representación latente de relleno (rellena con ceros) para la etapa B del procesamiento de Stable Cascade, con 4 canales y dimensiones basadas en el tamaño de la imagen de entrada dividido por 2. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/es.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
