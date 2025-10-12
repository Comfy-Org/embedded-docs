> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/es.md)

El nodo CLIPTextEncodeControlnet procesa texto de entrada utilizando un modelo CLIP y lo combina con datos de condicionamiento existentes para crear una salida de condicionamiento mejorada para aplicaciones de controlnet. Tokeniza el texto de entrada, lo codifica a través del modelo CLIP y añade los embeddings resultantes a los datos de condicionamiento proporcionados como parámetros de controlnet de atención cruzada.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Requerido | - | - | El modelo CLIP utilizado para la tokenización y codificación de texto |
| `condicionamiento` | CONDITIONING | Requerido | - | - | Datos de condicionamiento existentes que se mejorarán con parámetros de controlnet |
| `texto` | STRING | Multilínea, Prompts Dinámicos | - | - | Texto de entrada que será procesado por el modelo CLIP |

**Nota:** Este nodo requiere tanto las entradas `clip` como `conditioning` para funcionar correctamente. La entrada `text` admite prompts dinámicos y texto multilínea para un procesamiento de texto flexible.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Datos de condicionamiento mejorados con parámetros de atención cruzada de controlnet añadidos |
