# Generación de Imágenes Kling

Kling Image Generation Node genera imágenes a partir de prompts de texto, con la opción de usar una imagen de referencia como guía. Crea una o más imágenes basadas en la descripción de texto y los ajustes de referencia, y luego devuelve las imágenes generadas como salida.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto positivo | STRING | Sí | Máximo 500 caracteres |
| `negative_prompt` | Prompt de texto negativo | STRING | Sí | Máximo 500 caracteres |
| `image_type` | Selección del tipo de referencia de imagen (avanzado). Se usa cuando se proporciona una imagen de referencia. | COMBO | Sí | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensidad de referencia para imágenes subidas por el usuario (predeterminado: 0.5, avanzado) | FLOAT | Sí | 0.0 - 1.0 |
| `human_fidelity` | Similitud de referencia del sujeto (predeterminado: 0.45, avanzado) | FLOAT | Sí | 0.0 - 1.0 |
| `model_name` | Selección de modelo para generación de imágenes (predeterminado: "kling-v3") | COMBO | Sí | `"kling-v3"`<br>`"kling-v2"` |
| `aspect_ratio` | Relación de aspecto para las imágenes generadas (predeterminado: "16:9") | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Número de imágenes generadas (predeterminado: 1) | INT | Sí | 1 - 9 |
| `image` | Imagen de referencia opcional | IMAGE | No | - |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla (predeterminado: 0) | INT | No | 0 - 2147483647 |

**Restricciones de los parámetros:**

- El parámetro `image` es opcional. Cuando se proporciona una imagen de referencia, `image_type` determina si se utiliza como referencia de sujeto o referencia de estilo. Cuando no se proporciona una imagen de referencia, `image_type` no se aplica.
- `prompt` debe contener al menos 1 carácter y como máximo 500 caracteres. `negative_prompt` puede estar vacío, pero está limitado a 500 caracteres.
- El parámetro `seed` es opcional y no garantiza resultados deterministas.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|-------------|-------------|-----------|
| `output` | Imagen(es) generada(s) según los parámetros de entrada. Cuando se solicita más de una imagen, todas se devuelven apiladas en un solo lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/es.md)

---
**Source fingerprint (SHA-256):** `165d18244870b5b4f34587633a5492e733ad0b0a923bb8c3e506319460321906`
