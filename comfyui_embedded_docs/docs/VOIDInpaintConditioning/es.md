# VOIDInpaintConditioning

El nodo `VOIDInpaintConditioning` prepara los datos de condicionamiento necesarios para el inpainting con modelos CogVideoX. Toma un video de origen y una quadmask preprocesada, los codifica a través del VAE y los combina en una señal de condicionamiento de 32 canales (16 canales de máscara + 16 canales de video enmascarado) que el modelo utiliza para rellenar las áreas enmascaradas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo que se ampliará con la información latente de inpainting | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo que se ampliará con la información latente de inpainting | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la máscara y el video enmascarado en el espacio latente | VAE | Sí | - |
| `video` | Fotogramas de video de origen [T, H, W, 3] | IMAGE | Sí | - |
| `quadmask` | Quadmask preprocesada procedente de VOIDQuadmaskPreprocess [T, H, W] | MASK | Sí | - |
| `width` | El ancho al que se redimensionarán el video y la máscara (predeterminado: 672) | INT | Sí | 16 a MAX_RESOLUTION (step: 8) |
| `height` | La altura a la que se redimensionarán el video y la máscara (predeterminado: 384) | INT | Sí | 16 a MAX_RESOLUTION (step: 8) |
| `length` | Número de fotogramas de píxeles a procesar. Para CogVideoX-Fun-V1.5 (patch_size_t=2), `latent_t` debe ser par; las longitudes que producen `latent_t` impar se redondean hacia abajo (p. ej., 49 → 45) (predeterminado: 45) | INT | Sí | 1 a MAX_RESOLUTION (step: 1) |
| `batch_size` | El tamaño del lote para el latente de ruido de salida (predeterminado: 1) | INT | Sí | 1 a 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo con la información latente de inpainting añadida | CONDITIONING |
| `negative` | El condicionamiento negativo con la información latente de inpainting añadida | CONDITIONING |
| `latent` | Un tensor latente de ruido relleno de ceros con forma [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/es.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
