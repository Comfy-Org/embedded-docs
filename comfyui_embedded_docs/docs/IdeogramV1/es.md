# Ideogram V1

El nodo IdeogramV1 genera imágenes utilizando el modelo Ideogram V1 a través de una API. Toma indicaciones de texto y varias configuraciones de generación para crear una o más imágenes según tu entrada. El nodo admite diferentes relaciones de aspecto y modos de generación para personalizar el resultado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Indicación para la generación de la imagen (predeterminado: vacío) | STRING | Sí | - |
| `turbo` | Si se debe usar el modo turbo (generación más rápida, calidad potencialmente inferior) (predeterminado: False) | BOOLEAN | Sí | - |
| `aspect_ratio` | La relación de aspecto para la generación de la imagen (predeterminado: "1:1") | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `magic_prompt_option` | Determina si se debe usar MagicPrompt en la generación (predeterminado: "AUTO") | COMBO | No | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Valor de semilla aleatoria para la generación (predeterminado: 0) | INT | No | 0-2147483647 |
| `negative_prompt` | Descripción de lo que se debe excluir de la imagen (predeterminado: vacío) | STRING | No | - |
| `num_images` | Número de imágenes a generar (predeterminado: 1) | INT | No | 1-8 |

**Nota:** El parámetro `num_images` tiene un límite máximo de 8 imágenes por solicitud de generación.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La(s) imagen(es) generada(s) por el modelo Ideogram V1 | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/es.md)

---
**Source fingerprint (SHA-256):** `7e453cd54b5db48588ed899b0754e0d06fdcfbaed248d13fb74b7049f0f25b8f`
