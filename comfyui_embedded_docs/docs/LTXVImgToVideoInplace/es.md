> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/es.md)

El nodo LTXVImgToVideoInplace condiciona una representación latente de video codificando una imagen de entrada en sus fotogramas iniciales. Funciona utilizando un VAE para codificar la imagen en el espacio latente y luego mezclándola con las muestras latentes existentes según una fuerza especificada. Esto permite que una imagen sirva como punto de partida o señal de condicionamiento para la generación de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen de entrada en el espacio latente. |
| `image` | IMAGE | Sí | - | La imagen de entrada que se codificará y utilizará para condicionar el latente de video. |
| `latent` | LATENT | Sí | - | La representación latente de video objetivo que se va a modificar. |
| `strength` | FLOAT | No | 0.0 - 1.0 | Controla la fuerza de mezcla de la imagen codificada en el latente. Un valor de 1.0 reemplaza completamente los fotogramas iniciales, mientras que valores más bajos los mezclan. (por defecto: 1.0) |
| `bypass` | BOOLEAN | No | - | Omite el condicionamiento. Cuando está activado, el nodo devuelve el latente de entrada sin cambios. (por defecto: False) |

**Nota:** La `image` se redimensionará automáticamente para que coincida con las dimensiones espaciales requeridas por el `vae` para la codificación, basándose en el ancho y alto de la entrada `latent`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latent` | LATENT | La representación latente de video modificada. Contiene las muestras actualizadas y una `noise_mask` que aplica la fuerza de condicionamiento a los fotogramas iniciales. |
