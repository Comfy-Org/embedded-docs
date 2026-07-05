# VOIDInpaintConditioning

El nodo VOIDInpaintConditioning prepara los datos de condicionamiento necesarios para la pintura inteligente (inpainting) con modelos CogVideoX. Toma un video fuente y una cuadrimáscara (quadmask) preprocesada, los codifica a través del VAE y los combina en una señal de condicionamiento de 32 canales que el modelo utiliza para rellenar las áreas enmascaradas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo que se aumentará con la información latente de pintura inteligente | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo que se aumentará con la información latente de pintura inteligente | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la máscara y el video enmascarado en el espacio latente | VAE | Sí | - |
| `video` | Fotogramas del video fuente [T, H, W, 3] | IMAGE | Sí | - |
| `quadmask` | Cuadrimáscara preprocesada de VOIDQuadmaskPreprocess [T, H, W] | MASK | Sí | - |
| `width` | El ancho al que redimensionar el video y la máscara (predeterminado: 672) | INT | Sí | 16 a MAX_RESOLUTION (paso: 8) |
| `height` | La altura al que redimensionar el video y la máscara (predeterminado: 384) | INT | Sí | 16 a MAX_RESOLUTION (paso: 8) |
| `length` | Número de fotogramas de píxeles a procesar. Para CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t debe ser par — las longitudes que producen latent_t impar se redondean hacia abajo (ej. 49 → 45) (predeterminado: 45) | INT | Sí | 1 a MAX_RESOLUTION (paso: 1) |
| `batch_size` | El tamaño del lote para el latente de ruido de salida (predeterminado: 1) | INT | Sí | 1 a 64 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo con la información latente de pintura inteligente añadida | CONDITIONING |
| `negative` | El condicionamiento negativo con la información latente de pintura inteligente añadida | CONDITIONING |
| `latent` | Un tensor latente de ruido relleno con ceros con forma [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/es.md)

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
