> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/es.md)

El nodo Get Video Components extrae todos los elementos principales de un archivo de video. Separa el video en fotogramas individuales, extrae la pista de audio y proporciona información sobre la tasa de fotogramas del video. Esto permite trabajar con cada componente de forma independiente para su posterior procesamiento o análisis.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El video del cual extraer los componentes. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | Los fotogramas individuales extraídos del video como imágenes separadas. |
| `audio` | AUDIO | La pista de audio extraída del video. |
| `fps` | FLOAT | La tasa de fotogramas del video en fotogramas por segundo. |