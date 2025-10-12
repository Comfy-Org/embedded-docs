> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/es.md)

El nodo Kling Lip Sync Text to Video sincroniza los movimientos de la boca en un archivo de video para que coincidan con un texto. Toma un video de entrada y genera un nuevo video donde los movimientos labiales del personaje están alineados con el texto proporcionado. El nodo utiliza síntesis de voz para crear una sincronización del habla de aspecto natural.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | Archivo de video de entrada para la sincronización labial |
| `texto` | STRING | Sí | - | Contenido de texto para la generación de video con sincronización labial. Requerido cuando el modo es text2video. Longitud máxima: 120 caracteres. |
| `voz` | COMBO | No | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | Selección de voz para el audio de sincronización labial (por defecto: "Melody") |
| `velocidad_de_voz` | FLOAT | No | 0.8-2.0 | Velocidad del habla. Rango válido: 0.8~2.0, preciso a un decimal. (por defecto: 1) |

**Requisitos del Video:**
- El archivo de video no debe ser mayor a 100MB
- La altura/ancho debe estar entre 720px y 1920px
- La duración debe estar entre 2s y 10s

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `id_video` | VIDEO | Video generado con audio sincronizado labialmente |
| `duración` | STRING | Identificador único para el video generado |
| `duration` | STRING | Información de duración para el video generado |