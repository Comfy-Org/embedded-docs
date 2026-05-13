> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/es.md)

El nodo de generación de video a partir de imagen Vidu Q3 crea una secuencia de video a partir de una imagen de entrada. Utiliza un modelo Vidu Q3 para animar la imagen, guiado opcionalmente por un texto descriptivo, y genera un archivo de video como salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` | Modelo a utilizar para la generación de video. |
| `model.resolution` | COMBO | Sí | `"720p"`<br>`"1080p"`<br>`"2K"` (solo viduq3-pro) | Resolución del video de salida. Las opciones disponibles dependen del modelo seleccionado. |
| `model.duration` | INT | Sí | 1 a 16 | Duración del video de salida en segundos (predeterminado: 5). |
| `model.audio` | BOOLEAN | Sí | `True` / `False` | Cuando está habilitado, genera video con sonido (incluyendo diálogos y efectos de sonido) (predeterminado: False). |
| `imagen` | IMAGE | Sí | - | Imagen que se usará como fotograma inicial del video generado. |
| `prompt` | STRING | No | - | Texto descriptivo opcional para la generación del video (máximo 2000 caracteres) (predeterminado: vacío). |
| `semilla` | INT | No | 0 a 2147483647 | Valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1). |

**Nota:** La `image` debe tener una relación de aspecto entre 1:4 y 4:1 (vertical a horizontal). El `prompt` es opcional pero no puede exceder los 2000 caracteres. Las opciones de `model.resolution` dependen del `model` seleccionado: `"viduq3-pro"` admite `"720p"`, `"1080p"` y `"2K"`; `"viduq3-turbo"` admite `"720p"` y `"1080p"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `1dd3929860ee4a04b761014fd2cf7e9e32f9171d8b18fe1e93f27d0905ca04ee`
