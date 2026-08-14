# MiniMax H3 Primer-Último Fotograma a Video

Este nodo genera un video a partir de una imagen de primer fotograma y una imagen opcional de último fotograma utilizando el modelo MiniMax H3. El video respeta la relación de aspecto de las imágenes proporcionadas y, cuando se proporciona un último fotograma, anima desde el primer fotograma hacia el último.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model` | Modelo a utilizar para la generación de video. Al seleccionar un modelo, se muestran sus ajustes específicos (prompt, resolución, duración). | COMBO | Sí | "MiniMax H3" |
| `first_frame` | Imagen del primer fotograma para el video. La relación de aspecto del video generado sigue esta imagen. Debe tener al menos 256x256 píxeles con una relación de aspecto ancho-alto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `last_frame` | Imagen opcional del último fotograma para el video. Cuando se proporciona, el video comienza desde el primer fotograma y termina en esta imagen. Debe cumplir los mismos requisitos de tamaño y relación de aspecto que `first_frame`. | IMAGE | No | - |
| `seed` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos. Incluye una opción de "control después de generar" para aleatorizar después de cada generación. Valor predeterminado: 42. | INT | Sí | 0 a 4294967295 |
| `watermark` | Si se debe añadir una marca de agua AIGC al video. Este es un parámetro avanzado. Valor predeterminado: False. | BOOLEAN | Sí | True<br>False |

### MiniMax H3 Entradas

Estas entradas aparecen cuando se selecciona "MiniMax H3" en el selector `model`.

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `prompt` | Prompt de texto para la generación de video. Debe contener al menos un carácter que no sea espacio en blanco. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. | COMBO | Sí | "768P"<br>"2K" |
| `duration` | Duración del video de salida en segundos (4-15). Valor predeterminado: 5. | INT | Sí | 4 a 15 |

**Nota sobre las restricciones:**
- El prompt de texto dentro del combo `model` no puede estar vacío; los prompts que contienen solo espacios en blanco se rechazan.
- Cualquier imagen de fotograma proporcionada (`first_frame` y, si se usa, `last_frame`) debe tener al menos 256 píxeles de ancho y 256 píxeles de alto, con una relación de aspecto ancho-alto entre 0.4 y 2.5 (aproximadamente de 2:5 a 5:2).
- `last_frame` es opcional. Si se omite, el video se genera solo a partir del primer fotograma.
- La relación de aspecto del video de salida está determinada por las imágenes proporcionadas, no por una configuración de relación separada.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `video` | El video generado a partir del primer fotograma y del último fotograma opcional utilizando el modelo MiniMax H3. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `5c9fadf20f994950df9f1b0630fdce1416fe4459ad23bcd20dfa6f22adbe4598`
