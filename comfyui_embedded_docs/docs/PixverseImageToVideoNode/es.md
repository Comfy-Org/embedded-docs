# PixVerse Imagen a Video

Genera videos basados en una imagen de entrada y una indicación de texto. Este nodo toma una imagen y crea un video animado aplicando la configuración de movimiento y calidad especificada para transformar la imagen estática en una secuencia en movimiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | Imagen de entrada para transformar en video | IMAGE | Sí | - |
| `prompt` | Indicación para la generación del video | STRING | Sí | - |
| `calidad` | Configuración de calidad del video (predeterminado: res_540p) | COMBO | Sí | `res_540p`<br>`res_1080p` |
| `duración_en_segundos` | Duración del video generado en segundos | COMBO | Sí | `dur_2`<br>`dur_5`<br>`dur_10` |
| `modo_de_movimiento` | Estilo de movimiento aplicado a la generación del video | COMBO | Sí | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `semilla` | Semilla para la generación del video (predeterminado: 0) | INT | Sí | 0-2147483647 |
| `prompt_negativo` | Una descripción de texto opcional de los elementos no deseados en una imagen | STRING | No | - |
| `plantilla_pixverse` | Una plantilla opcional para influir en el estilo de la generación, creada por el nodo PixVerse Template | CUSTOM | No | - |

**Nota:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en normal y la duración se limita a 5 segundos. Para duraciones distintas de 5 segundos, el modo de movimiento también se establece automáticamente en normal.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | Video generado basado en la imagen y los parámetros de entrada | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
