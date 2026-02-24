> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/es.md)

El nodo CLIPTextEncodeKandinsky5 prepara los prompts de texto para su uso con el modelo Kandinsky 5. Toma dos entradas de texto separadas, las tokeniza utilizando un modelo CLIP proporcionado y las combina en una única salida de acondicionamiento. Esta salida se utiliza para guiar el proceso de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | | El modelo CLIP utilizado para tokenizar y codificar los prompts de texto. |
| `clip_l` | STRING | Sí | | El prompt de texto principal. Esta entrada admite texto multilínea y prompts dinámicos. |
| `qwen25_7b` | STRING | Sí | | Un prompt de texto secundario. Esta entrada admite texto multilínea y prompts dinámicos. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de acondicionamiento combinados generados a partir de ambos prompts de texto, listos para ser introducidos en un modelo Kandinsky 5 para la generación de imágenes. |
