# Referencia a video Grok

El nodo Grok Reference-to-Video genera un video a partir de un prompt de texto, utilizando hasta siete imágenes de referencia para guiar el estilo y el contenido de la salida. Con el modelo `grok-imagine-video-1.5`, también puedes adjuntar hasta tres referencias de voz predefinidas y hacer referencia a imágenes y voces directamente en el prompt usando las etiquetas `@ImageN` y `@AudioN`. El nodo envía la solicitud a una API externa, espera a que se complete la generación y descarga el video resultante.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo a utilizar para la generación de video. | DYNAMIC_COMBO | Sí | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `prompt` | Descripción de texto del video deseado. Debe ser una cadena no vacía. | STRING | Sí | N/A |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | No | 0 a 2147483647 |

### Entradas de Grok Imagine Video 1.5

Disponible cuando `model` se establece en `grok-imagine-video-1.5`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | Referencia de voz predefinida opcional; haz referencia a ella en el prompt como @Audio1. La API solo admite estas voces predefinidas, no audio personalizado (por defecto: none). | COMBO | No | Opciones de voz predefinidas, incluyendo `"none"` |
| `voice_2` | Segunda referencia de voz opcional; @Audio2 en el prompt (por defecto: none). | COMBO | No | Opciones de voz predefinidas, incluyendo `"none"` |
| `voice_3` | Tercera referencia de voz opcional; @Audio3 en el prompt (por defecto: none). | COMBO | No | Opciones de voz predefinidas, incluyendo `"none"` |
| `resolution` | La resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `aspect_ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La duración del video de salida en segundos (por defecto: 6). | INT | Sí | 1 a 15 |

### Entradas de Grok Imagine Video

Disponible cuando `model` se establece en `grok-imagine-video`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `resolution` | La resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `aspect_ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | La duración del video de salida en segundos (por defecto: 6). | INT | Sí | 2 a 10 |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Ranura ampliable: conecta de 1 a 7 imágenes de referencia para guiar la generación de video. Con `grok-imagine-video-1.5`, haz referencia a ellas en el prompt como @Image1 ... @Image7, numeradas en orden de entrada; una entrada por lotes cuenta una vez por imagen. | IMAGE | Sí | 1 a 7 imágenes |

**Nota:** Los subparámetros mostrados dependen del `model` seleccionado; `grok-imagine-video-1.5` añade las entradas `voice_1`, `voice_2` y `voice_3`. Se requiere al menos una imagen de referencia, y el total está limitado a 7 (una entrada por lotes cuenta una vez por imagen). Con `grok-imagine-video-1.5`, el prompt puede hacer referencia a las imágenes conectadas como `@Image1` ... `@Image7` y a las ranuras de voz como `@Audio1`, `@Audio2`, `@Audio3`; un `@image` o `@audio` sin numerar se refiere al primero. `@AudioN` se refiere al widget `voice_N`, no al orden de las voces habilitadas. Hacer referencia a una imagen no conectada o a una ranura de voz configurada como `none` causa un error. La API solo admite voces predefinidas, no audio personalizado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `ac068b34ad7efe786d29f51052a623eaf324041a99b124f6b5f81fadea661a83`
