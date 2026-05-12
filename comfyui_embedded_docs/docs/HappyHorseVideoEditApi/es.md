> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/es.md)

# Descripción General

Edite un video usando instrucciones de texto o imágenes de referencia con el modelo HappyHorse. La duración de salida coincide con el video de entrada (3-15 segundos), y las entradas de más de 15 segundos se truncan automáticamente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | DICT | Sí | Ver abajo | Configuración del modelo que contiene la selección del modelo, instrucción, resolución, relación de aspecto e imágenes de referencia opcionales. |
| `video` | VIDEO | Sí | - | El video a editar. |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla a utilizar para la generación (predeterminado: 0). |
| `watermark` | BOOLEAN | No | Verdadero / Falso | Si se debe agregar una marca de agua generada por IA al resultado (predeterminado: Falso). |

### Detalles del Parámetro `model`

El parámetro `model` es un diccionario con los siguientes campos:

| Campo | Tipo de Dato | Obligatorio | Rango | Descripción |
|-------|--------------|-------------|-------|-------------|
| `model` | STRING | Sí | `"happyhorse-1.0-video-edit"` | El modelo de edición de video HappyHorse a utilizar. |
| `prompt` | STRING | Sí | - | Instrucciones de edición o requisitos de transferencia de estilo. Debe tener al menos 1 carácter de longitud. |
| `resolution` | STRING | Sí | `"720P"`<br>`"1080P"` | La resolución de salida. |
| `ratio` | STRING | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Relación de aspecto. Si no se modifica, se aproxima a la relación de aspecto del video de entrada. |
| `reference_images` | DICT | No | 0 a 5 imágenes | Imágenes de referencia opcionales (imagen1, imagen2, imagen3, imagen4, imagen5) para guiar la edición. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El video editado de salida. |