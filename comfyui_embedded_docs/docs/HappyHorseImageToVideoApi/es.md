> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/es.md)

# Descripción General

Este nodo genera un video corto a partir de una única imagen inicial utilizando el modelo HappyHorse. Proporcionas una imagen de primer fotograma y un mensaje de texto que describe el movimiento y la escena deseados, y el nodo crea un video que continúa a partir de esa imagen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | COMBO | Sí | `"happyhorse-1.0-i2v"` | El modelo HappyHorse a utilizar para la generación de video. |
| `model.prompt` | STRING | No | N/A | Mensaje que describe los elementos y características visuales. Compatible con inglés y chino. (predeterminado: "") |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video de salida. (predeterminado: "720P") |
| `model.duration` | INT | Sí | 3 a 15 | La duración del video generado en segundos. (predeterminado: 5) |
| `first_frame` | IMAGE | Sí | N/A | Imagen del primer fotograma. La relación de aspecto de salida se deriva de esta imagen. |
| `seed` | INT | No | 0 a 2147483647 | Semilla a utilizar para la generación. (predeterminado: 0) |
| `watermark` | BOOLEAN | No | Verdadero / Falso | Si se debe agregar una marca de agua de IA generada al resultado. (predeterminado: Falso) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
