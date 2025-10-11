> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/es.md)

El nodo AudioEncoderLoader carga modelos de codificadores de audio desde tus archivos de codificadores de audio disponibles. Toma un nombre de archivo de codificador de audio como entrada y devuelve un modelo de codificador de audio cargado que puede utilizarse para tareas de procesamiento de audio en tu flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder_name` | STRING | COMBO | - | Archivos de codificadores de audio disponibles | Selecciona qué archivo de modelo de codificador de audio cargar desde tu carpeta audio_encoders |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Devuelve el modelo de codificador de audio cargado para usar en flujos de trabajo de procesamiento de audio |