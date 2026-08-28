# Generación de video de imagen a video Vidu Q3

El nodo Vidu Q3 Image-to-Video Generation crea una secuencia de video a partir de una imagen de entrada. Utiliza un modelo Vidu Q3 para animar la imagen, opcionalmente guiado por un prompt de texto, y produce un archivo de video.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la generación de video. | DYNAMIC_COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `imagen` | Una imagen que se utilizará como fotograma inicial del video generado. | IMAGE | Sí | - |
| `prompt` | Un prompt de texto opcional para la generación de video (máximo 2000 caracteres) (predeterminado: vacío). | STRING | Sí | - |
| `semilla` | Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1). Admite control posterior a la generación. | INT | Sí | 0 a 2147483647 |

### Entradas de viduq3-pro

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `duration` | Duración del video de salida en segundos (predeterminado: 5). | INT | Sí | 1 a 16 |
| `audio` | Cuando está habilitado, genera video con sonido (incluyendo diálogos y efectos de sonido) (predeterminado: False). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de viduq3-turbo

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `duration` | Duración del video de salida en segundos (predeterminado: 5). | INT | Sí | 1 a 16 |
| `audio` | Cuando está habilitado, genera video con sonido (incluyendo diálogos y efectos de sonido) (predeterminado: False). | BOOLEAN | Sí | `True`<br>`False` |

**Nota:** El parámetro `image` debe tener una relación de aspecto entre 1:4 y 4:1 (de vertical a horizontal). El parámetro `prompt` es opcional pero no puede superar los 2000 caracteres. Las opciones de resolución dependen del modelo seleccionado: `"viduq3-pro"` admite `"720p"`, `"1080p"` y `"2K"`; `"viduq3-turbo"` admite `"720p"` y `"1080p"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`
