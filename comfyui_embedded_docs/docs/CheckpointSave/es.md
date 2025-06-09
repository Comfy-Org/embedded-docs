El nodo `Guardar Punto de Control` está diseñado para guardar un modelo completo de Stable Diffusion (incluyendo los componentes UNet, CLIP y VAE) como un archivo de punto de control en formato **.safetensors**.

Este nodo se utiliza principalmente en flujos de trabajo de fusión de modelos. Después de crear un nuevo modelo fusionado a través de nodos como `ModelMergeSimple`, `ModelMergeBlocks`, etc., puede usar este nodo para guardar el resultado como un archivo de punto de control reutilizable.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `modelo` | MODEL | Representa el modelo principal cuyo estado se guardará. Es esencial para capturar el estado actual del modelo para su futura restauración o análisis. |
| `clip` | CLIP | Los parámetros del modelo CLIP asociado con el modelo principal, permitiendo que su estado se guarde junto con el modelo principal. |
| `vae` | VAE | Los parámetros del modelo Autoencoder Variacional (VAE), permitiendo que su estado se guarde junto con el modelo principal y CLIP para su uso o análisis futuro. |
| `prefijo_nombre_archivo` | STRING | Especifica el prefijo para el nombre del archivo del punto de control que se guardará. |

Además, el nodo tiene dos entradas ocultas para metadatos:

**prompt (PROMPT)**: Información del flujo de trabajo
**extra_pnginfo (EXTRA_PNGINFO)**: Información adicional del PNG

## Salidas

Este nodo generará un archivo de punto de control, y la ruta del archivo de salida correspondiente es el directorio `output/checkpoints/`

## Compatibilidad de Arquitecturas

- Actualmente con soporte completo: SDXL, SD3, SVD y otras arquitecturas principales, ver [código fuente](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Soporte básico: Otras arquitecturas pueden guardarse pero sin información de metadatos estandarizada

## Enlaces Relacionados

Código fuente relacionado: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)
