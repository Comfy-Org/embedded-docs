El nodo `StableCascade_SuperResolutionControlnet` prepara las entradas para el procesamiento de superresolución de Stable Cascade. Toma una imagen de entrada y la codifica usando un VAE para crear la entrada de controlnet, mientras también genera representaciones latentes placeholder para la etapa C y la etapa B del pipeline de Stable Cascade.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se procesará para superresolución | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen de entrada | VAE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `etapa_c` | La representación de imagen codificada adecuada para la entrada de controlnet | IMAGE |
| `etapa_b` | Representación latente placeholder para la etapa C del procesamiento de Stable Cascade | LATENT |
| `stage_b` | Representación latente placeholder para la etapa B del procesamiento de Stable Cascade | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/es.md)

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
