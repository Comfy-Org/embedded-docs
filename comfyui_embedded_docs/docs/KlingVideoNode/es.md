> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/es.md)

Este nodo genera videos utilizando el modelo Kling V3. Admite dos modos principales: texto a video, donde se crea un video a partir de una descripción textual, e imagen a video, donde se anima una imagen existente. También ofrece funciones avanzadas como la creación de videos multi-segmento con diferentes prompts para cada parte (storyboards) y la generación opcional de audio acompañante.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `multi_shot` | COMBO | Sí | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Controla si se genera un solo video o una serie de segmentos con prompts y duraciones individuales. Cuando no es "disabled", aparecen entradas adicionales para el prompt y la duración de cada storyboard. |
| `generate_audio` | BOOLEAN | Sí | `True` / `False` | Cuando está habilitado, el nodo generará audio para el video. El valor predeterminado es `True`. |
| `model` | COMBO | Sí | `"kling-v3"` | El modelo y su configuración asociada. Seleccionar esta opción revela los subparámetros `resolution` y `aspect_ratio`. |
| `model.resolution` | COMBO | Sí | `"1080p"`<br>`"720p"` | La resolución para el video generado. Esta configuración está disponible cuando `model` está configurado en "kling-v3". |
| `model.aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La relación de aspecto para el video generado. Esta configuración se ignora cuando se proporciona una imagen para `start_frame` (modo imagen a video). Disponible cuando `model` está configurado en "kling-v3". |
| `seed` | INT | Sí | 0 a 2147483647 | Un valor de semilla para la generación. Cambiar este valor hará que el nodo se vuelva a ejecutar, pero los resultados no son deterministas. El valor predeterminado es `0`. |
| `start_frame` | IMAGE | No | - | Una imagen de inicio opcional. Cuando está conectada, el nodo cambia del modo texto a video al modo imagen a video, animando la imagen proporcionada. |

**Entradas para el modo `multi_shot`:**
*   Cuando `multi_shot` está configurado en **"disabled"**, aparecen las siguientes entradas:
    *   `prompt` (STRING): La descripción de texto principal para el video. Obligatoria. Debe tener entre 1 y 2500 caracteres.
    *   `negative_prompt` (STRING): Texto que describe lo que no debe aparecer en el video. Opcional.
    *   `duration` (INT): La duración del video en segundos. Debe estar entre 3 y 15. El valor predeterminado es `5`.
*   Cuando `multi_shot` está configurado en una opción de storyboard (ej., `"3 storyboards"`), aparecen entradas para cada segmento del storyboard (ej., `storyboard_1_prompt`, `storyboard_1_duration`). Cada prompt debe tener entre 1 y 512 caracteres. **La suma total de todas las duraciones de los storyboards** debe estar entre 3 y 15 segundos.

**Restricciones:**
*   El nodo opera en modo **texto a video** cuando `start_frame` no está conectado. Utiliza la configuración `model.aspect_ratio` en este modo.
*   El nodo opera en modo **imagen a video** cuando `start_frame` está conectado. La configuración `model.aspect_ratio` se ignora. La imagen de entrada debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.
*   En el modo storyboard (`multi_shot` no es "disabled"), las entradas principales `prompt` y `negative_prompt` están ocultas y no se utilizan.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video generado. |