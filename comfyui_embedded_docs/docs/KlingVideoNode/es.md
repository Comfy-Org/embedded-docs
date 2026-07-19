# Kling 3.0 Video

Este nodo genera videos utilizando el modelo Kling V3. Admite dos modos principales: texto a video, donde se crea un video a partir de una descripción textual, e imagen a video, donde se anima una imagen existente. También ofrece funciones avanzadas como la creación de videos de múltiples segmentos con diferentes indicaciones para cada parte (guiones gráficos) y la opción de generar audio de acompañamiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `multi_shot` | Controla si se genera un solo video o una serie de segmentos con indicaciones y duraciones individuales. Cuando no está en "disabled", aparecen entradas adicionales para la indicación y duración de cada guión gráfico. | COMBO | Sí | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generar audio` | Cuando está habilitado, el nodo generará audio para el video. El valor predeterminado es `True`. | BOOLEAN | Sí | `True` / `False` |
| `modelo` | El modelo y sus ajustes asociados. Seleccionar esta opción revela los subparámetros `resolution` y `aspect_ratio`. | COMBO | Sí | `"kling-v3"` |
| `model.resolution` | La resolución del video generado. Este ajuste está disponible cuando el `modelo` está configurado en "kling-v3". | COMBO | Sí | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | La relación de aspecto del video generado. Este ajuste se ignora cuando se proporciona una imagen para `fotograma inicial` (modo imagen a video). Disponible cuando el `modelo` está configurado en "kling-v3". | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `semilla` | Un valor de semilla para la generación. Cambiar este valor hará que el nodo se ejecute nuevamente, pero los resultados no son deterministas. El valor predeterminado es `0`. | INT | Sí | 0 a 2147483647 |
| `fotograma inicial` | Una imagen inicial opcional. Cuando está conectada, el nodo cambia del modo texto a video al modo imagen a video, animando la imagen proporcionada. | IMAGE | No | - |

**Entradas para el modo `multi_shot`:**

* Cuando `multi_shot` está configurado en **"disabled"**, aparecen las siguientes entradas:
  * `prompt` (STRING): La descripción textual principal del video. Obligatorio. Debe tener entre 1 y 2500 caracteres.
  * `negative_prompt` (STRING): Texto que describe lo que no debe aparecer en el video. Opcional.
  * `duration` (INT): La duración del video en segundos. Debe estar entre 3 y 15. El valor predeterminado es `5`.
* Cuando `multi_shot` está configurado en una opción de guión gráfico (por ejemplo, `"3 storyboards"`), aparecen entradas para cada segmento del guión gráfico (por ejemplo, `storyboard_1_prompt`, `storyboard_1_duration`). Cada indicación debe tener entre 1 y 512 caracteres. La **suma total de todas las duraciones de los guiones gráficos** debe estar entre 3 y 15 segundos.

**Restricciones:**

* El nodo opera en modo **texto a video** cuando `start_frame` no está conectado. Utiliza el ajuste `model.aspect_ratio` en este modo.
* El nodo opera en modo **imagen a video** cuando `start_frame` está conectado. El ajuste `model.aspect_ratio` se ignora. La imagen de entrada debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.
* En el modo de guión gráfico (`multi_shot` no está en "disabled"), las entradas principales `prompt` y `negative_prompt` están ocultas y no se utilizan.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `f7f827d657b1d057d273eba3215ce6848d3ea05c5f348e2f3fccccfdd030dfc3`
