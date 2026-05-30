> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/es.md)

# Descripción General

El nodo Krea 2 Image genera imágenes utilizando el modelo de IA Krea 2. Soporta dos variantes del modelo: Medium para ilustraciones expresivas y Large para fotorrealismo expresivo. Opcionalmente, puedes incluir un moodboard y hasta 10 referencias de estilo de imagen para influir en la imagen generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Prompt de texto para la imagen. |
| `modelo` | DICT | Sí | Ver abajo | Krea 2 Medium es mejor para ilustraciones expresivas; Krea 2 Large es mejor para fotorrealismo expresivo. |
| `semilla` | INT | Sí | 0 a 2147483647 | Semilla aleatoria para reproducibilidad (predeterminado: 0). |

El parámetro `model` es un diccionario con los siguientes subparámetros:

| Subparámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|---------------|-----------|----------|-------|-------------|
| `modelo` | STRING | Sí | `"krea 2 medium"`<br>`"krea 2 large"` | Selecciona la variante del modelo Krea 2. |
| `aspect_ratio` | STRING | Sí | N/A | La relación de aspecto para la imagen generada. |
| `resolution` | STRING | Sí | N/A | La resolución para la imagen generada. |
| `creativity` | FLOAT | Sí | N/A | Controla el nivel de creatividad de la generación. |
| `moodboard_id` | STRING | No | N/A | El UUID de un moodboard de Krea para influir en la imagen. Debe ser un UUID válido. |
| `moodboard_strength` | FLOAT | No | N/A | La intensidad de la influencia del moodboard (predeterminado: 0.35). |
| `style_reference` | LIST | No | 0 a 10 elementos | Una lista de referencias de estilo de imagen. Cada referencia debe tener una `url` (STRING) y `strength` (FLOAT). |

**Restricciones:**
- `moodboard_id` debe ser un UUID válido (ej., `"123e4567-e89b-12d3-a456-426614174000"`). Cópialo desde el sitio web de Krea.
- `style_reference` acepta un máximo de 10 referencias de estilo de imagen.
- El `prompt` debe tener al menos 1 carácter de longitud.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen generada como tensor. |

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
