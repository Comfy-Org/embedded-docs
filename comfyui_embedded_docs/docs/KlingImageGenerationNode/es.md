# Generación de Imágenes Kling

El nodo Kling Image Generation genera imágenes a partir de prompts de texto, con la opción de usar una imagen de referencia como guía. Crea una o más imágenes basadas en la descripción de texto y en la configuración de referencia, y devuelve las imágenes generadas como salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto positivo | STRING | Sí | Máximo 500 caracteres |
| `negative_prompt` | Prompt de texto negativo | STRING | Sí | Máximo 500 caracteres |
| `image_type` | Selección del tipo de referencia de imagen (avanzado). Obligatorio cuando se proporciona una imagen de referencia. | COMBO | Sí | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensidad de referencia para imágenes subidas por el usuario (predeterminado: 0.5, avanzado) | FLOAT | Sí | 0.0 - 1.0 |
| `human_fidelity` | Similitud de referencia del sujeto (predeterminado: 0.45, avanzado) | FLOAT | Sí | 0.0 - 1.0 |
| `model_name` | Selección del modelo para la generación de imágenes (predeterminado: "kling-v3") | COMBO | Sí | `"kling-v3"` |
| `aspect_ratio` | Relación de aspecto para las imágenes generadas (predeterminado: "16:9") | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Número de imágenes generadas (predeterminado: 1) | INT | Sí | 1 - 9 |
| `image` | Imagen de referencia opcional | IMAGE | No | - |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0) | INT | No | 0 - 2147483647 |

**Restricciones de parámetros:**

- El parámetro `image` es opcional. Cuando se proporciona una imagen de referencia, el parámetro `image_type` determina si la referencia se utiliza como referencia de sujeto o como referencia de estilo.
- Cuando no se proporciona una imagen de referencia, los ajustes relacionados con la referencia (`image_type`, `image_fidelity`, `human_fidelity`) no tienen efecto en el resultado.
- `prompt` y `negative_prompt` tienen una longitud máxima de 500 caracteres.
- El parámetro `seed` es opcional y no garantiza resultados deterministas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | Imágenes generadas según los parámetros de entrada. Cuando `n` es mayor que 1, se devuelven varias imágenes como un lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/es.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
