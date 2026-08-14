# HappyHorse Imagen a Video

Este nodo genera un video corto a partir de una única imagen inicial utilizando el modelo HappyHorse. Proporcionas una imagen de primer fotograma y un prompt de texto que describe el movimiento y la escena deseados, y el nodo crea un video que continúa a partir de esa imagen.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo HappyHorse que se usará para la generación del video. | COMBO | Sí | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | Imagen del primer fotograma. La relación de aspecto de la salida se deriva de esta imagen. | IMAGE | Sí | N/D |
| `seed` | Semilla a usar para la generación. (por defecto: 0) | INT | No | 0 a 2147483647 |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado. (opción avanzada; por defecto: False) | BOOLEAN | No | True / False |

### Entradas de happyhorse-1.1-i2v y happyhorse-1.0-i2v

Ambas versiones del modelo comparten el mismo conjunto de parámetros.

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model.prompt` | Prompt que describe los elementos y las características visuales. Admite inglés y chino. (por defecto: "") | STRING | No | N/D |
| `model.resolution` | La resolución del video de salida. (por defecto: "720P") | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.duration` | La duración del video generado, en segundos. (por defecto: 5) | INT | Sí | 3 a 15 |

Nota: La imagen de `first_frame` debe tener al menos 300x300 píxeles, y su relación de aspecto debe estar entre 1:2.5 y 2.5:1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`
