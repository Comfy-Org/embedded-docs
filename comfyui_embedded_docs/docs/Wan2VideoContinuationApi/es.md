# Wan 2.7 Continuación de Video

El nodo Wan 2.7 Video Continuation genera un nuevo segmento de video que continúa desde el final de un videoclip de entrada. Utiliza el modelo Wan 2.7 para sintetizar la continuación basándose en un prompt de texto y, opcionalmente, puede guiar el final hacia un fotograma objetivo específico.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo de generación de video a utilizar. | COMBO | Sí | `"wan2.7-i2v"` |
| `first_clip` | Video de entrada a partir del cual continuar. Duración: de 2s a 10s. La relación de aspecto de la salida se deriva de este video. | VIDEO | Sí | 2s to 10s |
| `last_frame` | Imagen del último fotograma. La continuación hará una transición hacia este fotograma. | IMAGE | No | - |
| `seed` | Semilla a utilizar para la generación. (por defecto: 0) | INT | Sí | 0 a 2147483647 |
| `prompt_extend` | Si se debe mejorar el prompt con asistencia de IA. (por defecto: True) | BOOLEAN | Sí | - |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado. (por defecto: False) | BOOLEAN | Sí | - |

### wan2.7-i2v Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model.prompt` | Prompt que describe los elementos y las características visuales. Admite inglés y chino. (por defecto: cadena vacía) | STRING | Sí | - |
| `model.negative_prompt` | Prompt negativo que describe lo que se debe evitar. (por defecto: cadena vacía) | STRING | Sí | - |
| `model.resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.duration` | Duración total de la salida en segundos. El modelo genera la continuación para completar el tiempo restante después del clip de entrada. (por defecto: 5) | INT | Sí | 2 a 15 |

**Nota:** El video de entrada `first_clip` debe tener una duración de entre 2 y 10 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La continuación de video generada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/es.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`
