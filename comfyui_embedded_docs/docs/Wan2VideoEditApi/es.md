# Wan 2.7 Edición de Video

El nodo Wan2VideoEditApi utiliza el modelo Wan 2.7 para editar un video según instrucciones de texto, imágenes de referencia o transferencia de estilo. Procesa el video de entrada y genera un nuevo video de acuerdo con parámetros específicos como resolución, duración y relación de aspecto.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo a utilizar para la edición de video. | COMBO | Sí | `"wan2.7-videoedit"` |
| `video` | El video a editar. | VIDEO | Sí | - |
| `seed` | Semilla a utilizar para la generación. (por defecto: 0) | INT | No | 0 a 2147483647 |
| `audio_setting` | 'auto': el modelo decide si regenera el audio según el prompt. 'origin': conserva el audio original del video de entrada. (por defecto: "auto") | COMBO | No | `"auto"`<br>`"origin"` |
| `watermark` | Si se añade una marca de agua generada por IA al resultado. (por defecto: False) | BOOLEAN | No | - |

### Entradas de wan2.7-videoedit

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Instrucciones de edición o requisitos de transferencia de estilo. (por defecto: cadena vacía) | STRING | Sí | - |
| `resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `ratio` | Relación de aspecto. Si no se cambia, se aproxima a la relación del video de entrada. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Duración de salida en segundos. 'auto' coincide con la duración del video de entrada. Un valor específico trunca desde el inicio del video. (por defecto: "auto") | COMBO | Sí | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `reference_images` | Ranura ampliable: conecta de 0 a 4 imágenes (`image1`...`image4`) para guiar la edición. El límite de cantidad es 4 para el modelo wan2.7-videoedit. | IMAGE | No | 0 a 4 elementos |

**Restricciones:**
*   El `prompt` debe contener al menos 1 carácter.
*   El `video` de entrada debe tener una duración de entre 2 y 10 segundos.
*   La ranura ampliable `reference_images` acepta un máximo de 4 imágenes.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video editado generado por el modelo. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/es.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
