> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/es.md)

El nodo IdeogramV1 genera imágenes utilizando el modelo Ideogram V1 a través de una API. Toma indicaciones de texto y varias configuraciones de generación para crear una o más imágenes según tu entrada. El nodo admite diferentes relaciones de aspecto y modos de generación para personalizar el resultado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación para la generación de la imagen (predeterminado: vacío) |
| `turbo` | BOOLEAN | Sí | - | Si se debe usar el modo turbo (generación más rápida, calidad potencialmente inferior) (predeterminado: False) |
| `aspect_ratio` | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | La relación de aspecto para la generación de la imagen (predeterminado: "1:1") |
| `magic_prompt_option` | COMBO | No | "AUTO"<br>"ON"<br>"OFF" | Determina si se debe usar MagicPrompt en la generación (predeterminado: "AUTO") |
| `seed` | INT | No | 0-2147483647 | Valor de semilla aleatoria para la generación (predeterminado: 0) |
| `negative_prompt` | STRING | No | - | Descripción de lo que se debe excluir de la imagen (predeterminado: vacío) |
| `num_images` | INT | No | 1-8 | Número de imágenes a generar (predeterminado: 1) |

**Nota:** El parámetro `num_images` tiene un límite máximo de 8 imágenes por solicitud de generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La(s) imagen(es) generada(s) por el modelo Ideogram V1 |

---
**Source fingerprint (SHA-256):** `7e453cd54b5db48588ed899b0754e0d06fdcfbaed248d13fb74b7049f0f25b8f`
