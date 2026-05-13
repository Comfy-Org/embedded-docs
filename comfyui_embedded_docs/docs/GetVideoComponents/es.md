> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/es.md)

El nodo **Obtener Componentes de Video** extrae todos los elementos principales de un archivo de video. Separa el video en fotogramas individuales, extrae la pista de audio y proporciona la información de la tasa de fotogramas del video. Esto permite trabajar con cada componente de forma independiente para su posterior procesamiento o análisis.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | - | El video del cual extraer los componentes. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `audio` | IMAGE | Los fotogramas individuales extraídos del video como imágenes separadas. |
| `fps` | AUDIO | La pista de audio extraída del video. |
| `fps` | FLOAT | La tasa de fotogramas del video en fotogramas por segundo. |

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`
