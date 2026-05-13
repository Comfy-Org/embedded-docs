> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/es.md)

El nodo Ideogram V2 genera imágenes utilizando el modelo de IA Ideogram V2. Acepta indicaciones de texto y diversas configuraciones de generación para crear imágenes a través de un servicio API. El nodo admite diferentes relaciones de aspecto, resoluciones y opciones de estilo para personalizar las imágenes de salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación para la generación de la imagen (predeterminado: cadena vacía) |
| `turbo` | BOOLEAN | No | - | Si se debe usar el modo turbo (generación más rápida, calidad potencialmente inferior) (predeterminado: Falso) |
| `aspect_ratio` | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | La relación de aspecto para la generación de la imagen. Se ignora si la resolución no está configurada en AUTO. (predeterminado: "1:1") |
| `resolution` | COMBO | No | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La resolución para la generación de la imagen. Si no está configurada en AUTO, anula la configuración de `aspect_ratio`. (predeterminado: "Auto") |
| `magic_prompt_option` | COMBO | No | "AUTO"<br>"ON"<br>"OFF" | Determina si se debe usar MagicPrompt en la generación (predeterminado: "AUTO") |
| `seed` | INT | No | 0-2147483647 | Semilla aleatoria para la generación (predeterminado: 0) |
| `style_type` | COMBO | No | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | Tipo de estilo para la generación (solo V2) (predeterminado: "NONE") |
| `negative_prompt` | STRING | No | - | Descripción de lo que se debe excluir de la imagen (predeterminado: cadena vacía) |
| `num_images` | INT | No | 1-8 | Número de imágenes a generar (predeterminado: 1) |

**Nota:** Cuando `resolution` no está configurado en "Auto", anula la configuración de `aspect_ratio`. El parámetro `num_images` tiene un límite máximo de 8 imágenes por generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La(s) imagen(es) generada(s) por el modelo Ideogram V2 |

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
