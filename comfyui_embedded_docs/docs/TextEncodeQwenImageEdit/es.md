> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/es.md)

El nodo TextEncodeQwenImageEdit procesa prompts de texto e imágenes opcionales para generar datos de condicionamiento para generación o edición de imágenes. Utiliza un modelo CLIP para tokenizar la entrada y puede opcionalmente codificar imágenes de referencia usando un VAE para crear latentes de referencia. Cuando se proporciona una imagen, esta se redimensiona automáticamente para mantener dimensiones de procesamiento consistentes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización de texto e imágenes |
| `prompt` | STRING | Sí | - | Prompt de texto para la generación de condicionamiento, admite entrada multilínea y prompts dinámicos |
| `vae` | VAE | No | - | Modelo VAE opcional para codificar imágenes de referencia en latentes |
| `image` | IMAGE | No | - | Imagen de entrada opcional para fines de referencia o edición |

**Nota:** Cuando se proporcionan tanto `image` como `vae`, el nodo codifica la imagen en latentes de referencia y los adjunta a la salida de condicionamiento. La imagen se redimensiona automáticamente para mantener una escala de procesamiento consistente de aproximadamente 1024x1024 píxeles.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Datos de condicionamiento que contienen tokens de texto y latentes de referencia opcionales para generación de imágenes |
