# VOIDInpaintConditioning

El nodo VOIDInpaintConditioning prepara los datos de acondicionamiento necesarios para el inpainting con modelos CogVideoX. Toma un video fuente y una quadmask preprocesada, los codifica a través del VAE y los combina en una señal de acondicionamiento de 32 canales (16 canales de la máscara + 16 canales del video enmascarado) que el modelo utiliza para rellenar las áreas enmascaradas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo que se aumentará con la información latente de inpainting | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo que se aumentará con la información latente de inpainting | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la máscara y el video enmascarado en el espacio latente | VAE | Sí | - |
| `video` | Fotogramas del video fuente [T, H, W, 3] | IMAGE | Sí | - |
| `quadmask` | Quadmask preprocesada de VOIDQuadmaskPreprocess [T, H, W] | MASK | Sí | - |
| `width` | El ancho al que se redimensionarán el video y la máscara (predeterminado: 672) | INT | Sí | 16 a MAX_RESOLUTION (paso: 8) |
| `height` | El alto al que se redimensionarán el video y la máscara (predeterminado: 384) | INT | Sí | 16 a MAX_RESOLUTION (paso: 8) |
| `length` | Número de fotogramas de píxeles a procesar. Para CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t debe ser par — las longitudes que producen latent_t impar se redondean hacia abajo (p. ej. 49 → 45) (predeterminado: 45) | INT | Sí | 1 a MAX_RESOLUTION (paso: 1) |
| `batch_size` | El tamaño de lote para el ruido latente de salida (predeterminado: 1) | INT | Sí | 1 a 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo con la información latente de inpainting añadida | CONDITIONING |
| `negative` | El condicionamiento negativo con la información latente de inpainting añadida | CONDITIONING |
| `latent` | Un tensor de ruido latente relleno de ceros con forma [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/es.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
