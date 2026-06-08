El nodo `AudioEncoderLoader` carga un modelo de codificador de audio desde un archivo en tu carpeta de codificadores de audio. Toma como entrada el nombre de archivo de un modelo de codificador de audio y devuelve el modelo cargado, que luego puede utilizarse para tareas de procesamiento de audio en tu flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre_codificador_audio` | Selecciona qué archivo de modelo de codificador de audio cargar | STRING | Sí | Lista de archivos de codificador de audio disponibles en la carpeta audio_encoders |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio_encoder` | El modelo de codificador de audio cargado, listo para usar en flujos de trabajo de procesamiento de audio | AUDIO_ENCODER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/es.md)

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`
