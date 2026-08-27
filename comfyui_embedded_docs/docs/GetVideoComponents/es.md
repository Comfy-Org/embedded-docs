# Obtener componentes de video

El nodo Get Video Components extrae todos los elementos principales de un archivo de video. Separa el video en fotogramas individuales, extrae la pista de audio y proporciona la velocidad de fotogramas, la profundidad de bits y la información del espacio de color del video. Esto permite trabajar con cada componente de forma independiente para su posterior procesamiento o análisis.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `video` | El video del que se extraen los componentes. | VIDEO | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imágenes` | Los fotogramas individuales extraídos del video como imágenes separadas. | IMAGE |
| `audio` | La pista de audio extraída del video. | AUDIO |
| `fps` | La velocidad de fotogramas del video en fotogramas por segundo. | FLOAT |
| `bit_depth` | La profundidad de bits del video. | INT |
| `color_space` | El espacio de color del video. | COMBO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/es.md)

---
**Source fingerprint (SHA-256):** `ffe8b6c698cb9a855b8796768f068d403448cf56188ce4c5ead21bff30baff6e`
