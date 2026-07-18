# Guardar Audio (Avanzado)

Guarda el audio de entrada en tu directorio de salida de ComfyUI. Este nodo permite exportar audio en varios formatos, incluyendo FLAC, MP3 y Opus, con ajustes de calidad configurables.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `audio` | El audio a guardar. | AUDIO | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir tokens de formato como %date:yyyy-MM-dd%. (predeterminado: "audio/ComfyUI") | STRING | Sí | - |
| `formato` | El formato de archivo en el cual guardar el audio. | COMBO | Sí | "flac"<br>"mp3"<br>"opus" |

Cuando se selecciona "mp3" como formato, un subparámetro `quality` estará disponible con las siguientes opciones: "V0", "128k", "320k" (predeterminado: "V0").

Cuando se selecciona "opus" como formato, un subparámetro `quality` estará disponible con las siguientes opciones: "64k", "96k", "128k", "192k", "320k" (predeterminado: "128k").

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `audio` | Salida de interfaz de usuario que contiene la información del archivo de audio guardado. | UI |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `98314263dd84c562e7c02ba89f3d10551fcb898ac784af2aa397ca8357e4aae8`
