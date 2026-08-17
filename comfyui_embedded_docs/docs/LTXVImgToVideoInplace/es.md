# LTXVImgToVideoInplace

El nodo LTXVImgToVideoInplace condiciona una representación latente de video codificando una imagen de entrada en sus fotogramas iniciales. Funciona usando un VAE para codificar la imagen en el espacio latente y luego reemplazando los primeros fotogramas de las muestras latentes de video con esta imagen codificada. Se aplica una máscara de ruido para que la fuerza de condicionamiento controle cuán fuertemente influye la imagen en esos fotogramas iniciales durante la generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar la imagen de entrada en el espacio latente. | VAE | Sí | - |
| `image` | La imagen de entrada que se codificará y se usará para condicionar el latente de video. | IMAGE | Sí | - |
| `latent` | La representación latente de video objetivo que se modificará. | LATENT | Sí | - |
| `strength` | Controla la fuerza de condicionamiento de la imagen codificada en los fotogramas latentes iniciales. Un valor de 1.0 condiciona completamente los fotogramas iniciales, mientras que valores más bajos aplican un condicionamiento más débil. (por defecto: 1.0) | FLOAT | No | 0.0 - 1.0 |
| `bypass` | Omitir el condicionamiento. Cuando está habilitado, el nodo devuelve el latente de entrada sin cambios. (por defecto: False) | BOOLEAN | No | - |

**Nota:** La `image` se redimensionará automáticamente (interpolación bilineal) para ajustarse a las dimensiones espaciales requeridas por la `vae` para la codificación, según el ancho y alto del `latent` de entrada. Solo se utilizan los primeros 3 canales de color (RGB) de la imagen; cualquier canal alfa se ignora.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latent` | La representación latente de video modificada. Contiene las muestras actualizadas y una `noise_mask` que aplica la fuerza de condicionamiento a los fotogramas iniciales. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/es.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
