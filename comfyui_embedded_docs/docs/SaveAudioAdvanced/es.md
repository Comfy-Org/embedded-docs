# Guardar audio (avanzado)

Save Audio (Avanzado)

Guarda el audio de entrada en el directorio de salida de ComfyUI. Puede exportar audio en formato FLAC, MP3 u Opus, con opciones de calidad seleccionables para archivos MP3 y Opus.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `format` | El formato de archivo en el que se guardará el audio. | DYNAMIC_COMBO | Sí | "flac"<br>"mp3"<br>"opus" |
| `audio` | El audio a guardar. | AUDIO | Sí | - |
| `filename_prefix` | El prefijo para el archivo a guardar. Puede incluir tokens de formato como %date:yyyy-MM-dd%. (predeterminado: "audio/ComfyUI") | STRING | Sí | - |

### Entradas de flac

El formato `flac` no requiere ajustes adicionales.

### Entradas de mp3

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `quality` | La calidad de codificación para archivos MP3. (predeterminado: "V0") | COMBO | Sí | "V0"<br>"128k"<br>"320k" |

### Entradas de opus

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `quality` | La calidad de codificación para archivos Opus. (predeterminado: "128k") | COMBO | Sí | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**Nota:** El ajuste `quality` solo se muestra cuando `format` es `mp3` u `opus`. Si no se proporciona un valor de `quality`, el audio se guarda utilizando la calidad predeterminada del formato seleccionado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El audio de entrada, pasado después de guardarse. | AUDIO |
| `ui` | Salida de interfaz que contiene la información del archivo de audio guardado. | UI |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
