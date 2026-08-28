# Kling 3.0 Video

Este nodo genera vídeos utilizando el modelo Kling V3. Admite el modo de texto a vídeo, en el que se crea un vídeo a partir de una descripción textual, y el modo de imagen a vídeo, en el que se anima una imagen existente. También ofrece funciones avanzadas como la creación de vídeos de varios segmentos con indicaciones individuales para cada parte (storyboards) y la generación opcional de audio de acompañamiento.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `multi_shot` | Genera una serie de segmentos de vídeo con indicaciones y duraciones individuales. Cuando se establece en una opción de storyboard, aparecen entradas adicionales para la indicación y la duración de cada storyboard. | DYNAMIC_COMBO | Sí | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `modelo` | Modelo y ajustes de generación. Al seleccionar un modelo, se muestran sus subparámetros de resolución y relación de aspecto. | DYNAMIC_COMBO | Sí | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `generar audio` | Cuando está habilitado, el nodo genera audio para el vídeo. Nota: `"kling-3.0-turbo"` siempre genera audio nativo, por lo que esta opción se ignora para ese modelo. El valor predeterminado es True. | BOOLEAN | Sí | True<br>False |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. El valor predeterminado es 0. | INT | Sí | 0 a 2147483647 |
| `fotograma inicial` | Imagen opcional de fotograma inicial. Cuando está conectada, cambia al modo de imagen a vídeo. | IMAGE | No | - |

### Entradas de kling-v3

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `resolución` | La resolución del vídeo generado. El valor predeterminado es `"1080p"`. | COMBO | Sí | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `relación de aspecto` | La relación de aspecto del vídeo generado. Se ignora en el modo de imagen a vídeo. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entradas de kling-3.0-turbo

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `resolución` | La resolución del vídeo generado. El valor predeterminado es `"720p"`. | COMBO | Sí | `"1080p"`<br>`"720p"` |
| `relación de aspecto` | La relación de aspecto del vídeo generado. Se ignora en el modo de imagen a vídeo. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entradas de Multi-shot

**Cuando `multi_shot` se establece en `"disabled"`:**

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | La descripción textual principal del vídeo. Debe tener entre 1 y 2500 caracteres. | STRING | Sí | 1 a 2500 caracteres |
| `negative_prompt` | Texto que describe lo que no debe aparecer en el vídeo. Puede dejarse vacío. | STRING | No | - |
| `duration` | La duración del vídeo en segundos. El valor predeterminado es 5. | INT | Sí | 3 a 15 |

**Cuando `multi_shot` se establece en una opción de storyboard (por ejemplo, `"3 storyboards"`):**

Para cada segmento de storyboard N (del 1 hasta el número de storyboards seleccionado), aparecen las siguientes entradas:

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `storyboard_N_prompt` | Indicación para el segmento de storyboard N. Máximo 512 caracteres. | STRING | Sí | 1 a 512 caracteres |
| `storyboard_N_duration` | Duración del segmento de storyboard N en segundos. El valor predeterminado es 4. | INT | Sí | 1 a 15 |

**Restricciones y comportamiento:**

- El modo de texto a vídeo se utiliza cuando `start_frame` no está conectado; el modo de imagen a vídeo se utiliza cuando `start_frame` está conectado. En el modo de imagen a vídeo, `model.aspect_ratio` se ignora y la imagen de entrada debe tener al menos 300x300 píxeles con una relación de aspecto entre 1:2.5 y 2.5:1.
- En el modo storyboard, la `prompt` principal y `negative_prompt` no se utilizan. La suma total de todas las duraciones de los storyboards debe estar entre 3 y 15 segundos.
- `negative_prompt` solo se utiliza con `kling-v3`; se ignora cuando se selecciona `kling-3.0-turbo`.
- Para `kling-v3`, cada storyboard se envía a la API como un segmento separado. Para `kling-3.0-turbo`, las indicaciones y duraciones de los storyboards se combinan en una única indicación multi-shot.
- Para `kling-3.0-turbo`, `generate_audio` se ignora porque este modelo siempre genera audio nativo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `video` | El archivo de vídeo generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
