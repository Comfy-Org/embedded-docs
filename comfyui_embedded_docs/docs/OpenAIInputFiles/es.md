> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/es.md)

Carga y formatea archivos de entrada para la API de OpenAI. Este nodo prepara archivos de texto (.txt) y PDF (.pdf) para incluirlos como contexto de entrada en el Nodo de Chat de OpenAI. Los archivos serán leídos por el modelo de OpenAI al generar una respuesta. Se pueden encadenar varios nodos de Archivos de Entrada de OpenAI para incluir varios archivos en un solo mensaje.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `archivo` | COMBO | Sí | Múltiples opciones disponibles (todos los archivos .txt y .pdf en el directorio de entrada menores a 32MB) | Archivos de entrada para incluir como contexto para el modelo. Por ahora solo acepta archivos de texto (.txt) y PDF (.pdf). Los archivos deben ser menores a 32MB. |
| `ARCHIVOS_ENTRADA_OPENAI` | OPENAI_INPUT_FILES | No | N/A | Un archivo o archivos adicionales opcionales para agrupar junto con el archivo cargado desde este nodo. Permite encadenar archivos de entrada para que un solo mensaje pueda incluir múltiples archivos de entrada. |

**Restricciones de Archivos:**

- Solo se admiten archivos .txt y .pdf
- Tamaño máximo de archivo: 32MB
- Los archivos se cargan desde el directorio de entrada de ComfyUI

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `ARCHIVOS_ENTRADA_OPENAI` | OPENAI_INPUT_FILES | Archivos de entrada formateados listos para usarse como contexto en llamadas a la API de OpenAI. |

---
**Source fingerprint (SHA-256):** `e5e92f6628072da9af787867e38c89dde3db853b7289ef6c607a066cd04c1cc9`
