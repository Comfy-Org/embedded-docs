# Kling 3.0 Video

Este nodo genera videos utilizando el modelo Kling V3. Admite el modo texto-a-video, donde se crea un video a partir de una descripción de texto, y el modo imagen-a-video, donde se anima una imagen existente. También ofrece funciones avanzadas como la creación de videos de múltiples segmentos con indicaciones individuales para cada parte (storyboards) y, opcionalmente, la generación de audio de acompañamiento.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `multi_shot` | Genera una serie de segmentos de video con indicaciones y duraciones individuales. Cuando se selecciona una opción de storyboard, aparecen entradas adicionales para la indicación y la duración de cada storyboard. | COMBO | Sí | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `model` | Configuración del modelo y de la generación. Al seleccionar un modelo se muestran sus subparámetros `model.resolution` y `model.aspect_ratio`. | COMBO | Sí | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `generate_audio` | Cuando está habilitado, el nodo genera audio para el video. Nota: `"kling-3.0-turbo"` siempre genera audio nativo, por lo que este interruptor se ignora para ese modelo. El valor predeterminado es True. | BOOLEAN | Sí | True<br>False |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. El valor predeterminado es 0. | INT | Sí | 0 a 2147483647 |
| `start_frame` | Imagen de fotograma inicial opcional. Cuando está conectado, cambia al modo imagen-a-video. | IMAGE | No | - |

### Entradas de kling-v3

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model.resolution` | La resolución del video generado. El valor predeterminado es `"1080p"`. | COMBO | Sí | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | La relación de aspecto del video generado. Se ignora en el modo imagen-a-video. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entradas de kling-3.0-turbo

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model.resolution` | La resolución del video generado. El valor predeterminado es `"720p"`. | COMBO | Sí | `"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | La relación de aspecto del video generado. Se ignora en el modo imagen-a-video. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entradas de multi-shot

**Cuando `multi_shot` está configurado en `"disabled"`:**

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | La descripción de texto principal del video. Debe tener entre 1 y 2500 caracteres. | STRING | Sí | 1 a 2500 caracteres |
| `negative_prompt` | Texto que describe lo que no debe aparecer en el video. Puede dejarse vacío. | STRING | No | - |
| `duration` | La duración del video en segundos. El valor predeterminado es 5. | INT | Sí | 3 a 15 |

**Cuando `multi_shot` está configurado en una opción de storyboard (p. ej., `"3 storyboards"`):**

Para cada segmento de storyboard N (desde 1 hasta el número de storyboards seleccionado), aparecen las siguientes entradas:

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `storyboard_N_prompt` | Indicación para el segmento de storyboard N. Máximo 512 caracteres. | STRING | Sí | 1 a 512 caracteres |
| `storyboard_N_duration` | Duración para el segmento de storyboard N en segundos. El valor predeterminado es 4. | INT | Sí | 1 a 15 |

**Restricciones y comportamiento:**

- El modo texto-a-video se utiliza cuando `start_frame` no está conectado; el modo imagen-a-video se utiliza cuando `start_frame` está conectado. En el modo imagen-a-video, `model.aspect_ratio` se ignora y la imagen de entrada debe tener al menos 300x300 píxeles con una relación de aspecto entre 1:2.5 y 2.5:1.
- En el modo storyboard, la `prompt` principal y el `negative_prompt` no se utilizan. La suma total de todas las duraciones de los storyboards debe estar entre 3 y 15 segundos.
- Para `kling-v3`, cada storyboard se envía a la API como un segmento separado. Para `kling-3.0-turbo`, las indicaciones y duraciones de los storyboards se combinan en una única indicación de múltiples tomas (multi-shot).
- Para `kling-3.0-turbo`, `generate_audio` se ignora porque este modelo siempre genera audio nativo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
