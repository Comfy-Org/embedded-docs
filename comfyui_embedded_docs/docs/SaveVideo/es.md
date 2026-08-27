# Guardar video

El nodo Save Video guarda el vídeo de entrada en tu directorio de salida de ComfyUI. Puedes elegir el prefijo del nombre de archivo, el formato de contenedor, el códec de vídeo y las opciones de codificación, como la calidad y el espacio de color. El nodo gestiona automáticamente el nombre del archivo con incrementos de contador y puede incrustar metadatos del flujo de trabajo en el archivo guardado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El vídeo que se va a guardar. | VIDEO | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir información de formato, como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`, para incluir valores de nodos (predeterminado: "video/ComfyUI"). | STRING | Sí | - |
| `formato` | El contenedor de salida. Auto conserva el contenedor de origen cuando es posible; MP4, MKV y WebM seleccionan un contenedor específico (predeterminado: "auto"). | DYNAMIC_COMBO | Sí | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `códec` | El códec de vídeo de salida. Auto conserva una transmisión de origen compatible. La re-codificación H.264 y AV1 admite SDR, HDR (HLG) y HDR PQ. Aparece cuando se selecciona un formato (predeterminado: "auto"). | DYNAMIC_COMBO | No | `"auto"`<br>`"h264"`<br>`"av1"` |

### Entradas de H.264

Estas entradas aparecen cuando `codec` es `"h264"`. Este códec está disponible con los formatos `auto`, `mp4` y `mkv`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `encoding` | Automático conserva las transmisiones H.264 compatibles. Re-encode aplica opciones de codificación personalizadas. | DYNAMIC_COMBO | No | `"auto"`<br>`"re-encode"` |
| `crf` | Los valores más bajos producen mayor calidad y archivos más grandes. Aparece cuando `encoding` es `"re-encode"` (predeterminado: 23.0). | FLOAT | No | 0.0 a 51.0 |
| `color_space` | Auto utiliza sRGB para vídeos creados a partir de imágenes y conserva los colores reconocidos en vídeos cargados. sRGB escribe SDR BT.709/sRGB. HDR escribe BT.2020/HLG de 10 bits; HDR PQ escribe BT.2020/PQ. Otros píxeles de entrada ya deben usar el espacio de color seleccionado. Aparece cuando `encoding` es `"re-encode"` (predeterminado: "auto"). | COMBO | No | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### Entradas de AV1

Estas entradas aparecen cuando `codec` es `"av1"`. Este códec está disponible con los formatos `auto`, `mp4`, `mkv` y `webm`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `encoding` | Automático conserva las transmisiones AV1 compatibles. Re-encode aplica opciones de codificación personalizadas. | DYNAMIC_COMBO | No | `"auto"`<br>`"re-encode"` |
| `crf` | Los valores más bajos producen mayor calidad y archivos más grandes. Aparece cuando `encoding` es `"re-encode"` (predeterminado: 30.0). | FLOAT | No | 0.0 a 63.0 |
| `color_space` | Auto utiliza sRGB para vídeos creados a partir de imágenes y conserva los colores reconocidos en vídeos cargados. sRGB escribe SDR BT.709/sRGB. HDR escribe BT.2020/HLG de 10 bits; HDR PQ escribe BT.2020/PQ. Otros píxeles de entrada ya deben usar el espacio de color seleccionado. Aparece cuando `encoding` es `"re-encode"` (predeterminado: "auto"). | COMBO | No | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Nota: El formato `webm` solo admite los códecs `auto` y `av1`. Cuando `format` es `"auto"`, el contenedor de origen se conserva cuando es posible. Cuando `color_space` es `"auto"`, no se aplica ningún espacio de color explícito y el espacio de color se determina automáticamente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `video` | El vídeo de entrada, sin cambios. | VIDEO |
| `ui` | Una vista previa del archivo de vídeo guardado, incluida la ruta del archivo y la información de subcarpeta para mostrarla en la interfaz de usuario. | PREVIEW_VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/es.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
