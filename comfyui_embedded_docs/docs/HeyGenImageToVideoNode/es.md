# HeyGen Video 1.0 de imagen a vídeo

Anima una imagen para convertirla en un video con diálogo y sonido sincronizados usando HeyGen Video 1.0. La imagen conectada se usa como primer fotograma y el video generado mantiene su relación de aspecto. Describe lo que debe suceder, incluidas las líneas habladas, en el prompt. El nodo carga la imagen, crea el trabajo de video, espera a que finalice y devuelve el video resultante.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Versión del modelo utilizada para la generación. (predeterminado: `"heygen-video-1"`) | DYNAMIC_COMBO | Sí | `"heygen-video-1"` |
| `image` | Primer fotograma del video. Se requiere exactamente una imagen; se rechaza un lote. Recorta la imagen para cambiar la forma del video, porque la salida mantiene la relación de aspecto de esta imagen. | IMAGE | Sí | 1 imagen, relación de aspecto 1:4 a 4:1 |
| `prompt` | Descripción de lo que sucede en el video, incluido cualquier diálogo. (predeterminado: cadena vacía) | STRING | Sí | 1 a 16000 caracteres |
| `duration` | Duración del video de salida en segundos. Se ignora cuando `auto_duration` es `"enabled"`. (predeterminado: 5) | INT | Sí | 5 a 30 |
| `resolution` | Resolución de salida. (predeterminado: `"768p"`) | COMBO | Sí | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Semilla para la generación. Los resultados aún pueden variar entre ejecuciones con la misma semilla. (predeterminado: 42) | INT | Sí | 0 a 4294967295 |
| `auto_duration` | Cuando está habilitado, la duración del video sigue al diálogo entrecomillado en el prompt (8 a 30 segundos) y `duration` se ignora. (predeterminado: `"disabled"`) | COMBO | No | `"disabled"`<br>`"enabled"` |

### Restricciones de los parámetros

- **Imagen única:** `image` debe contener exactamente una imagen. Conectar un lote genera un error.
- **Relación de aspecto de la imagen:** la imagen no debe ser más ancha que 4 veces su altura ni más alta que 4 veces su anchura (entre 1:4 y 4:1); de lo contrario, la ejecución falla.
- **Prompt obligatorio:** el prompt debe contener al menos un carácter que no sea espacio en blanco y como máximo 16000 caracteres.
- **Semilla:** la semilla solo determina si el nodo se vuelve a ejecutar; los resultados no son reproducibles con la misma semilla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El video generado con diálogo y sonido sincronizados, con la relación de aspecto de la imagen de entrada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
