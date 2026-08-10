# MinimaxHailuo03FirstLastFrameNode

Este nodo genera un video a partir de una imagen de primer fotograma y, opcionalmente, una imagen de último fotograma, utilizando el modelo MiniMax H3. El video sigue la relación de aspecto de las imágenes proporcionadas y, cuando se incluye un último fotograma, se anima desde el primer fotograma hacia el último.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Modelo a utilizar para la generación del video. Este combo incluye la selección del modelo ("MiniMax H3"), un prompt de texto que describe el video a generar, la resolución de salida y la duración del video. El prompt debe contener al menos un carácter que no sea un espacio en blanco. | COMBO | Sí | "MiniMax H3" |
| `first_frame` | Imagen del primer fotograma del video. La relación de aspecto del video generado sigue la de esta imagen. Debe tener al menos 256x256 píxeles y una relación de aspecto ancho-alto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `last_frame` | Imagen opcional del último fotograma del video. Cuando se proporciona, el video comienza desde el primer fotograma y termina en esta imagen. Debe cumplir los mismos requisitos de tamaño y relación de aspecto que `first_frame`. | IMAGE | No | - |
| `seed` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos. Incluye una opción 'control after generate' para aleatorizar después de cada generación. Valor predeterminado: 42. | INT | Sí | 0 a 4294967295 |
| `watermark` | Indica si se debe añadir una marca de agua AIGC al video. Este es un parámetro avanzado. Valor predeterminado: False. | BOOLEAN | Sí | True<br>False |

**Nota sobre las restricciones:**
- El prompt de texto dentro del combo `model` no puede estar vacío; los prompts que contengan solo espacios en blanco son rechazados.
- Cualquier imagen de fotograma proporcionada (`first_frame` y, si se usa, `last_frame`) debe tener al menos 256 píxeles de ancho y 256 píxeles de alto, con una relación de aspecto ancho-alto entre 0.4 y 2.5 (aproximadamente de 2:5 a 5:2).
- `last_frame` es opcional. Cuando se omite, el video se genera solo a partir del primer fotograma.
- La relación de aspecto del video de salida está determinada por las imágenes proporcionadas, no por un ajuste de relación de aspecto independiente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video generado a partir del primer fotograma y, opcionalmente, del último fotograma, utilizando el modelo MiniMax H3. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `f4cb9217eb346019680c64b30c1beacce16f0050616b7b76265edc5840f6b21e`
