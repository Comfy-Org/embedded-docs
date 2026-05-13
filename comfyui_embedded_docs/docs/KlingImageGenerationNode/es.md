> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/es.md)

El nodo de generación de imágenes Kling crea imágenes a partir de descripciones textuales, con la opción de utilizar una imagen de referencia como guía. Genera una o más imágenes basadas en tu descripción de texto y configuración de referencia, y luego devuelve las imágenes generadas como resultado.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual positiva |
| `negative_prompt` | STRING | Sí | - | Descripción textual negativa |
| `image_type` | COMBO | Sí | `"subject_reference"`<br>`"style_reference"` | Selección del tipo de referencia de imagen (avanzado). Obligatorio cuando se proporciona una imagen de referencia. |
| `image_fidelity` | FLOAT | Sí | 0.0 - 1.0 | Intensidad de referencia para imágenes subidas por el usuario (predeterminado: 0.5, avanzado) |
| `human_fidelity` | FLOAT | Sí | 0.0 - 1.0 | Similitud de referencia del sujeto (predeterminado: 0.45, avanzado) |
| `model_name` | COMBO | Sí | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` | Selección del modelo para la generación de imágenes (predeterminado: "kling-v3") |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | Relación de aspecto para las imágenes generadas (predeterminado: "16:9") |
| `n` | INT | Sí | 1 - 9 | Número de imágenes generadas (predeterminado: 1) |
| `image` | IMAGE | No | - | Imagen de referencia opcional |
| `semilla` | INT | No | 0 - 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0) |

**Restricciones de los parámetros:**

- El parámetro `image` es opcional. Cuando se proporciona una imagen de referencia, el parámetro `image_type` debe configurarse como `"subject_reference"` o `"style_reference"`.
- Cuando no se proporciona una imagen de referencia, los parámetros `image_type`, `image_fidelity` y `human_fidelity` no se utilizan.
- La descripción textual positiva y negativa tienen una longitud máxima de `MAX_PROMPT_LENGTH_IMAGE_GEN` caracteres.
- El parámetro `seed` es opcional y no garantiza resultados deterministas.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | Imagen(es) generada(s) según los parámetros de entrada |

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
