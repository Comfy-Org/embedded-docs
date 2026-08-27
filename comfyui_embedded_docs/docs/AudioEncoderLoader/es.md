# CargadorCodificadorAudio

El nodo AudioEncoderLoader carga un modelo de codificador de audio desde un archivo en tu carpeta de codificadores de audio. Toma el nombre de archivo de un modelo de codificador de audio como entrada y devuelve el modelo cargado, que luego puede utilizarse para tareas de procesamiento de audio en tu flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre_codificador_audio` | Selecciona qué archivo de modelo de codificador de audio cargar | COMBO | Sí | Lista de archivos de codificador de audio disponibles en la carpeta audio_encoders |

Nota: Si el archivo seleccionado no contiene un modelo de codificador de audio válido, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `audio_encoder` | El modelo de codificador de audio cargado, listo para usar en flujos de trabajo de procesamiento de audio | AUDIO_ENCODER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/es.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
