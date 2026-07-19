# HappyHorse Edición de Video

Edite un vídeo utilizando instrucciones de texto o imágenes de referencia con el modelo HappyHorse. La duración de salida es de 3 a 15 segundos y coincide con el vídeo de entrada; las entradas de más de 15 segundos se truncan.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Configuración del modelo que contiene la selección del modelo, instrucción, resolución, relación de aspecto e imágenes de referencia opcionales. | DICT | Sí | Ver más abajo |
| `video` | El vídeo a editar. | VIDEO | Sí | - |
| `semilla` | Semilla a utilizar para la generación (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `marca de agua` | Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: Falso). | BOOLEAN | No | Verdadero / Falso |

### Detalles del Parámetro `model`

El parámetro `model` es un diccionario con los siguientes campos:

| Campo | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de edición de vídeo HappyHorse a utilizar. | STRING | Sí | `"happyhorse-1.0-video-edit"` |
| `prompt` | Instrucciones de edición o requisitos de transferencia de estilo. Debe tener al menos 1 carácter de longitud. | STRING | Sí | - |
| `resolution` | La resolución de salida. | STRING | Sí | `"720P"`<br>`"1080P"` |
| `ratio` | Relación de aspecto. Si no se modifica, se aproxima a la relación de aspecto del vídeo de entrada. | STRING | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `reference_images` | Imágenes de referencia opcionales (image1, image2, image3, image4, image5) para guiar la edición. | DICT | No | 0 a 5 imágenes |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | La salida del vídeo editado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/es.md)

---
**Source fingerprint (SHA-256):** `af6747efbea1c65e4909d35dad009cbc2ffaad787d0f2031581c227deb9bf53c`
