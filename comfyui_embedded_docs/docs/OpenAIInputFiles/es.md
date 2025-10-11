> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/es.md)

Carga y formatea archivos de entrada para la API de OpenAI. Este nodo prepara archivos de texto y PDF para incluirlos como entradas de contexto para el nodo OpenAI Chat. Los archivos serán leídos por el modelo de OpenAI al generar respuestas. Se pueden encadenar múltiples nodos de archivos de entrada para incluir varios archivos en un solo mensaje.

## Entradas

| Parámetro | Tipo de Datos | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `file` | COMBO | Sí | Múltiples opciones disponibles | Archivos de entrada para incluir como contexto para el modelo. Por ahora solo acepta archivos de texto (.txt) y PDF (.pdf). Los archivos deben ser menores a 32MB. |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | No | N/A | Archivo(s) adicional opcional para agrupar junto con el archivo cargado desde este nodo. Permite encadenar archivos de entrada para que un solo mensaje pueda incluir múltiples archivos de entrada. |

**Restricciones de Archivos:**
- Solo se admiten archivos .txt y .pdf
- Tamaño máximo de archivo: 32MB
- Los archivos se cargan desde el directorio de entrada

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|------------------|---------------|-------------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Archivos de entrada formateados listos para ser utilizados como contexto para las llamadas a la API de OpenAI. |