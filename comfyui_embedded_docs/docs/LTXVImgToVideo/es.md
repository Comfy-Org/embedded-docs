# LTXVImgToVideo

El nodo LTXVImgToVideo prepara una representación latente para generar un video a partir de una imagen de entrada. La imagen se redimensiona al ancho y alto solicitados, se codifica con el VAE y se coloca en los primeros fotogramas latentes. Se crea una máscara de ruido utilizando `strength` para controlar cuánto del contenido de la imagen original se preserva o modifica, y el condicionamiento positivo y negativo se transfieren sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Datos de condicionamiento positivo proporcionados como entrada y devueltos sin cambios. | CONDITIONING | Sí | - |
| `negative` | Datos de condicionamiento negativo proporcionados como entrada y devueltos sin cambios. | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar la imagen de entrada en el espacio latente. | VAE | Sí | - |
| `image` | Imagen de entrada que se redimensiona y codifica para formar el inicio del latente de video. | IMAGE | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 768, paso: 32). | INT | Sí | 64 a MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (predeterminado: 512, paso: 32). | INT | Sí | 64 a MAX_RESOLUTION |
| `length` | Número de fotogramas en el video generado (predeterminado: 97, paso: 8). | INT | Sí | 9 a MAX_RESOLUTION |
| `batch_size` | Número de videos a generar en un lote latente (predeterminado: 1). | INT | Sí | 1 a 4096 |
| `strength` | Controla cuánto del contenido de la imagen codificada se preserva en los primeros fotogramas latentes. Un valor de 1.0 preserva la imagen original por completo, mientras que 0.0 permite la modificación máxima (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 |

Nota: `MAX_RESOLUTION` es la resolución máxima permitida por la instalación de ComfyUI.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo transferido sin modificaciones. | CONDITIONING |
| `negative` | Condicionamiento negativo transferido sin modificaciones. | CONDITIONING |
| `latent` | Latente de video que contiene la imagen de entrada codificada al inicio de la secuencia, junto con una máscara de ruido basada en `strength`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/es.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
