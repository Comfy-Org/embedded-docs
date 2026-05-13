> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/es.md)

El nodo Ideogram V3 genera imágenes utilizando el modelo Ideogram V3. Admite tanto la generación de imágenes estándar a partir de indicaciones de texto como la edición de imágenes cuando se proporcionan tanto una imagen como una máscara. El nodo ofrece varios controles para la relación de aspecto, resolución, velocidad de generación e imágenes de referencia de personajes opcionales.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación para la generación o edición de la imagen (predeterminado: vacío) |
| `image` | IMAGE | No | - | Imagen de referencia opcional para edición de imágenes |
| `mask` | MASK | No | - | Máscara opcional para relleno generativo (las áreas blancas serán reemplazadas) |
| `aspect_ratio` | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | La relación de aspecto para la generación de imágenes. Se ignora si la resolución no está configurada en Auto (predeterminado: "1:1") |
| `resolution` | COMBO | No | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La resolución para la generación de imágenes. Si no está configurada en Auto, anula la configuración de relación de aspecto (predeterminado: "Auto") |
| `magic_prompt_option` | COMBO | No | "AUTO"<br>"ON"<br>"OFF" | Determina si se debe usar MagicPrompt en la generación (predeterminado: "AUTO") |
| `seed` | INT | No | 0-2147483647 | Semilla aleatoria para la generación (predeterminado: 0) |
| `num_images` | INT | No | 1-8 | Número de imágenes a generar (predeterminado: 1) |
| `rendering_speed` | COMBO | No | "DEFAULT"<br>"TURBO"<br>"QUALITY" | Controla la compensación entre velocidad de generación y calidad (predeterminado: "DEFAULT") |
| `imagen_personaje` | IMAGE | No | - | Imagen para usar como referencia de personaje |
| `máscara_personaje` | MASK | No | - | Máscara opcional para la imagen de referencia de personaje |

**Restricciones de parámetros:**

- Cuando se proporcionan tanto `image` como `mask`, el nodo cambia al modo de edición
- Si solo se proporciona uno de `image` o `mask`, se producirá un error
- `character_mask` requiere que `character_image` esté presente
- El parámetro `aspect_ratio` se ignora cuando `resolution` no está configurado en "Auto"
- Las áreas blancas en la máscara serán reemplazadas durante el relleno generativo
- La máscara de personaje y la imagen de personaje deben tener el mismo tamaño

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | IMAGE | La(s) imagen(es) generada(s) o editada(s) |

---
**Source fingerprint (SHA-256):** `0d0058cc8483c453100d8d9dfcb9a31ae5e686f38ced77ed7e472cd083c3464b`
