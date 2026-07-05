# Obtener componentes de video

El nodo **Obtener Componentes de Video** extrae todos los elementos principales de un archivo de video. Separa el video en fotogramas individuales, extrae la pista de audio y proporciona la información de la tasa de fotogramas del video. Esto permite trabajar con cada componente de forma independiente para su posterior procesamiento o análisis.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El video del cual extraer los componentes. | VIDEO | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imágenes` | Los fotogramas individuales extraídos del video como imágenes separadas. | IMAGE |
| `audio` | La pista de audio extraída del video. | AUDIO |
| `fps` | La tasa de fotogramas del video en fotogramas por segundo. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/es.md)

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`
