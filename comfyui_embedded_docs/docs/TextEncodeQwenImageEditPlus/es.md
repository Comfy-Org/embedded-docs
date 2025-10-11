> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/es.md)

El nodo TextEncodeQwenImageEditPlus procesa instrucciones de texto e imágenes opcionales para generar datos de condicionamiento para tareas de generación o edición de imágenes. Utiliza una plantilla especializada para analizar imágenes de entrada y comprender cómo las instrucciones de texto deben modificarlas, luego codifica esta información para su uso en pasos posteriores de generación. El nodo puede manejar hasta tres imágenes de entrada y opcionalmente generar latentes de referencia cuando se proporciona un VAE.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para tokenización y codificación |
| `prompt` | STRING | Sí | - | Instrucción de texto que describe la modificación de imagen deseada (admite entrada multilínea y prompts dinámicos) |
| `vae` | VAE | No | - | Modelo VAE opcional para generar latentes de referencia a partir de imágenes de entrada |
| `image1` | IMAGE | No | - | Primera imagen de entrada opcional para análisis y modificación |
| `image2` | IMAGE | No | - | Segunda imagen de entrada opcional para análisis y modificación |
| `image3` | IMAGE | No | - | Tercera imagen de entrada opcional para análisis y modificación |

**Nota:** Cuando se proporciona un VAE, el nodo genera latentes de referencia a partir de todas las imágenes de entrada. El nodo puede procesar hasta tres imágenes simultáneamente, y las imágenes se redimensionan automáticamente a dimensiones apropiadas para el procesamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Datos de condicionamiento codificados que contienen tokens de texto y latentes de referencia opcionales para la generación de imágenes |