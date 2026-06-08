El nodo Ideogram V2 genera imágenes utilizando el modelo de IA Ideogram V2. Acepta indicaciones de texto y diversas configuraciones de generación para crear imágenes a través de un servicio API. El nodo admite diferentes relaciones de aspecto, resoluciones y opciones de estilo para personalizar las imágenes de salida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Indicación para la generación de la imagen (predeterminado: cadena vacía) | STRING | Sí | - |
| `turbo` | Si se debe usar el modo turbo (generación más rápida, calidad potencialmente inferior) (predeterminado: Falso) | BOOLEAN | No | - |
| `aspect_ratio` | La relación de aspecto para la generación de la imagen. Se ignora si la resolución no está configurada en AUTO. (predeterminado: "1:1") | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `resolution` | La resolución para la generación de la imagen. Si no está configurada en AUTO, anula la configuración de `aspect_ratio`. (predeterminado: "Auto") | COMBO | No | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `magic_prompt_option` | Determina si se debe usar MagicPrompt en la generación (predeterminado: "AUTO") | COMBO | No | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Semilla aleatoria para la generación (predeterminado: 0) | INT | No | 0-2147483647 |
| `style_type` | Tipo de estilo para la generación (solo V2) (predeterminado: "NONE") | COMBO | No | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" |
| `negative_prompt` | Descripción de lo que se debe excluir de la imagen (predeterminado: cadena vacía) | STRING | No | - |
| `num_images` | Número de imágenes a generar (predeterminado: 1) | INT | No | 1-8 |

**Nota:** Cuando `resolution` no está configurado en "Auto", anula la configuración de `aspect_ratio`. El parámetro `num_images` tiene un límite máximo de 8 imágenes por generación.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La(s) imagen(es) generada(s) por el modelo Ideogram V2 | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/es.md)

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
