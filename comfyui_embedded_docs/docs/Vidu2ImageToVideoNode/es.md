> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/es.md)

El nodo de Generación de Video a partir de Imagen Vidu2 crea una secuencia de video a partir de una única imagen de entrada. Utiliza un modelo Vidu2 específico para animar la escena basándose en un mensaje de texto opcional, controlando la duración, resolución e intensidad del movimiento del video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | COMBO | Sí | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | El modelo Vidu2 a utilizar para la generación de video. Diferentes modelos ofrecen distintas compensaciones entre velocidad y calidad. |
| `image` | IMAGE | Sí | - | Una imagen que se usará como fotograma inicial del video generado. Solo se permite una imagen. |
| `prompt` | STRING | No | - | Un mensaje de texto opcional para la generación del video (máximo 2000 caracteres). El valor predeterminado es una cadena vacía. |
| `duration` | INT | Sí | 1 a 10 | La duración del video generado en segundos. El valor predeterminado es 5. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla para la generación de números aleatorios, con el fin de garantizar resultados reproducibles. El valor predeterminado es 1. |
| `resolution` | COMBO | Sí | `"720p"`<br>`"1080p"` | La resolución de salida del video generado. Este parámetro es avanzado. |
| `movement_amplitude` | COMBO | Sí | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | La amplitud de movimiento de los objetos en el fotograma. Este parámetro es avanzado. |

**Restricciones:**

* La entrada `image` debe contener exactamente una imagen.
* La relación de aspecto de la imagen de entrada debe estar entre 1:4 y 4:1.
* El texto de `prompt` está limitado a un máximo de 2000 caracteres.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `204f8d2b9edf17c2c180480f98a852718416a54725d92e5fec574b8517ada398`
