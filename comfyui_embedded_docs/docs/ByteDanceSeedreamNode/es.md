> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/es.md)

El nodo ByteDance Seedream 4 proporciona capacidades unificadas de generación de texto a imagen y edición precisa con oraciones individuales con resolución de hasta 4K. Puede crear nuevas imágenes a partir de prompts de texto o editar imágenes existentes usando instrucciones de texto. El nodo soporta tanto la generación de imágenes individuales como la generación secuencial de múltiples imágenes relacionadas.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | Nombre del modelo |
| `prompt` | STRING | STRING | "" | - | Prompt de texto para crear o editar una imagen. |
| `image` | IMAGE | IMAGE | - | - | Imagen(es) de entrada para generación de imagen a imagen. Lista de 1-10 imágenes para generación con referencia simple o múltiple. |
| `size_preset` | STRING | COMBO | Primer preset de RECOMMENDED_PRESETS_SEEDREAM_4 | Todas las etiquetas de RECOMMENDED_PRESETS_SEEDREAM_4 | Selecciona un tamaño recomendado. Selecciona Personalizado para usar el ancho y alto a continuación. |
| `width` | INT | INT | 2048 | 1024-4096 (paso 64) | Ancho personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` |
| `height` | INT | INT | 2048 | 1024-4096 (paso 64) | Alto personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | Modo de generación de imágenes grupales. 'disabled' genera una sola imagen. 'auto' permite al modelo decidir si generar múltiples imágenes relacionadas (ej. escenas de historias, variaciones de personajes). |
| `max_images` | INT | INT | 1 | 1-15 | Número máximo de imágenes a generar cuando sequential_image_generation='auto'. El total de imágenes (entrada + generadas) no puede exceder 15. |
| `seed` | INT | INT | 0 | 0-2147483647 | Semilla a usar para la generación. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Si añadir una marca de agua "Generado por IA" a la imagen. |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | Si está habilitado, aborta la ejecución si faltan algunas imágenes solicitadas o si devuelven un error. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Imagen(es) generada(s) basada(s) en los parámetros de entrada y el prompt |