> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/es.md)

Este nodo genera respuestas de texto a partir de un modelo de OpenAI. Permite mantener conversaciones con el modelo de IA mediante el envío de mensajes de texto y la recepción de respuestas generadas. El nodo admite conversaciones de múltiples turnos donde puede recordar el contexto previo, y también puede procesar imágenes y archivos como contexto adicional para el modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Entradas de texto para el modelo, utilizadas para generar una respuesta (valor por defecto: vacío) |
| `persist_context` | BOOLEAN | Sí | - | Conservar el contexto del chat entre llamadas para conversaciones de múltiples turnos (valor por defecto: True) |
| `model` | COMBO | Sí | Múltiples modelos de OpenAI disponibles | El modelo de OpenAI a utilizar para generar respuestas |
| `images` | IMAGE | No | - | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puede utilizar el nodo Batch Images (valor por defecto: None) |
| `files` | OPENAI_INPUT_FILES | No | - | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo OpenAI Chat Input Files (valor por defecto: None) |
| `advanced_options` | OPENAI_CHAT_CONFIG | No | - | Configuración opcional para el modelo. Acepta entradas del nodo OpenAI Chat Advanced Options (valor por defecto: None) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_text` | STRING | La respuesta de texto generada por el modelo de OpenAI |