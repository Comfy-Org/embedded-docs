# HappyHorse Imagen a Video

Este nodo genera un video corto a partir de una única imagen inicial utilizando el modelo HappyHorse. Proporcionas una imagen de primer fotograma y un mensaje de texto que describe el movimiento y la escena deseados, y el nodo crea un video que continúa a partir de esa imagen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo HappyHorse a utilizar para la generación de video. | COMBO | Sí | `"happyhorse-1.0-i2v"` |
| `model.prompt` | Mensaje que describe los elementos y características visuales. Compatible con inglés y chino. (predeterminado: "") | STRING | No | N/A |
| `model.resolution` | La resolución del video de salida. (predeterminado: "720P") | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.duration` | La duración del video generado en segundos. (predeterminado: 5) | INT | Sí | 3 a 15 |
| `primer fotograma` | Imagen del primer fotograma. La relación de aspecto de salida se deriva de esta imagen. | IMAGE | Sí | N/A |
| `semilla` | Semilla a utilizar para la generación. (predeterminado: 0) | INT | No | 0 a 2147483647 |
| `marca de agua` | Si se debe agregar una marca de agua de IA generada al resultado. (predeterminado: Falso) | BOOLEAN | No | Verdadero / Falso |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
