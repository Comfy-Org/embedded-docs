> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/es.md)

El nodo CLIP Text Encode for Lumina2 codifica un mensaje de sistema y un mensaje de usuario utilizando un modelo CLIP en una incrustación que puede guiar al modelo de difusión para generar imágenes específicas. Combina un mensaje de sistema predefinido con su mensaje de texto personalizado y los procesa a través del modelo CLIP para crear datos de condicionamiento para la generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `system_prompt` | STRING | COMBO | - | "superior", "alignment" | Lumina2 proporciona dos tipos de mensajes de sistema: Superior: Eres un asistente diseñado para generar imágenes superiores con un grado superior de alineación imagen-texto basado en mensajes textuales o mensajes de usuario. Alignment: Eres un asistente diseñado para generar imágenes de alta calidad con el mayor grado de alineación imagen-texto basado en mensajes textuales. |
| `user_prompt` | STRING | STRING | - | - | El texto que será codificado. |
| `clip` | CLIP | CLIP | - | - | El modelo CLIP utilizado para codificar el texto. |

**Nota:** La entrada `clip` es obligatoria y no puede ser None. Si la entrada clip no es válida, el nodo generará un error indicando que el checkpoint puede no contener un modelo CLIP o codificador de texto válido.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Un condicionamiento que contiene el texto incrustado utilizado para guiar al modelo de difusión. |
