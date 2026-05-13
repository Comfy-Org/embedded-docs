> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/es.md)

El nodo LTXVImgToVideoInplace condiciona una representación latente de video codificando una imagen de entrada en sus fotogramas iniciales. Funciona utilizando un VAE para codificar la imagen en el espacio latente y luego fusionándola con las muestras latentes existentes según una intensidad especificada. Esto permite que una imagen sirva como punto de partida o señal de condicionamiento para la generación de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen de entrada en el espacio latente. |
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se codificará y utilizará para condicionar el video latente. |
| `latente` | LATENT | Sí | - | La representación latente de video de destino que se modificará. |
| `fuerza` | FLOAT | No | 0.0 - 1.0 | Controla la intensidad de fusión de la imagen codificada en el latente. Un valor de 1.0 reemplaza completamente los fotogramas iniciales, mientras que valores más bajos los fusionan. (predeterminado: 1.0) |
| `omitir` | BOOLEAN | No | - | Omite el condicionamiento. Cuando está habilitado, el nodo devuelve el latente de entrada sin cambios. (predeterminado: False) |

**Nota:** La `image` se redimensionará automáticamente para que coincida con las dimensiones espaciales requeridas por el `vae` para la codificación, según el ancho y alto de la entrada `latent`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latente` | LATENT | La representación latente de video modificada. Contiene las muestras actualizadas y una `noise_mask` que aplica la intensidad de condicionamiento a los fotogramas iniciales. |

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
