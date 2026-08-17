# Guardar video

El nodo SaveVideo guarda un vídeo de entrada en tu directorio de salida de ComfyUI. Te permite elegir el prefijo del nombre de archivo, el formato de vídeo y el códec, y automáticamente crea un nombre de archivo único añadiendo un contador. Por defecto, el nodo también almacena los metadatos del flujo de trabajo en el vídeo guardado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `codec` | El códec que se usará para el vídeo. Seleccionar `h264` muestra opciones de codificación adicionales (predeterminado: "auto"). | DYNAMIC_COMBO | Sí | "auto"<br>"h264" |
| `video` | El vídeo que se guardará. | VIDEO | Sí | - |
| `filename_prefix` | El prefijo para el archivo a guardar. Puede incluir información de formato, como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`, para incluir valores de nodos (predeterminado: "video/ComfyUI"). | STRING | Sí | - |
| `format` | El formato en el que se guardará el vídeo. Esto determina la extensión de archivo del vídeo guardado (predeterminado: "auto"). | COMBO | Sí | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### Entradas h264

Estas entradas aparecen cuando `codec` está establecido en `h264`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `encoding` | El modo de codificación para H.264. Automatic conserva flujos H.264 compatibles. Re-encode aplica un CRF personalizado (predeterminado: "auto"). | DYNAMIC_COMBO | No | "auto"<br>"re-encode" |
| `crf` | Los valores más bajos producen mayor calidad y archivos más grandes. Solo disponible cuando `encoding` está establecido en `re-encode` (predeterminado: 23.0). | FLOAT | Sí (solo cuando `encoding` es `re-encode`) | 0.0 a 51.0 (paso: 1.0) |

Nota: Si `filename_prefix` incluye carpetas, por ejemplo `video/ComfyUI`, el vídeo se guarda dentro de esa subcarpeta del directorio de salida. El nombre del archivo se crea a partir del prefijo con un contador añadido, por ejemplo `ComfyUI_00001_.mp4`, de modo que los archivos existentes no se sobrescriben.

Nota: Cuando los metadatos están habilitados, el nodo incrusta el prompt del flujo de trabajo y metadatos adicionales en el vídeo guardado. Los metadatos se pueden deshabilitar iniciando ComfyUI con el argumento `--disable-metadata`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `video` | El vídeo que se guardó, pasado desde la entrada. | VIDEO |
| `ui` | Una vista previa del archivo de vídeo guardado, incluida la ruta del archivo y la información de la subcarpeta para mostrar en la interfaz de usuario. | PREVIEW_VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/es.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
