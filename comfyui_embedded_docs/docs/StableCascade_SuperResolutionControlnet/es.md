> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/es.md)

El nodo StableCascade_SuperResolutionControlnet prepara las entradas para el procesamiento de superresolución de Stable Cascade. Toma una imagen de entrada y la codifica utilizando un VAE para crear la entrada del controlnet, mientras también genera representaciones latentes de marcador de posición para la etapa C y la etapa B de la canalización de Stable Cascade.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se procesará para superresolución |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen de entrada |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | La representación de imagen codificada adecuada para la entrada del controlnet |
| `stage_c` | LATENT | Representación latente de marcador de posición para la etapa C del procesamiento de Stable Cascade |
| `stage_b` | LATENT | Representación latente de marcador de posición para la etapa B del procesamiento de Stable Cascade |