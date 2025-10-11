> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/es.md)

El nodo Ideogram V3 genera imágenes utilizando el modelo Ideogram V3. Soporta tanto la generación regular de imágenes a partir de prompts de texto como la edición de imágenes cuando se proporcionan tanto una imagen como una máscara. El nodo ofrece varios controles para la relación de aspecto, resolución, velocidad de generación e imágenes opcionales de referencia de personajes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación o edición de imagen (valor por defecto: vacío) |
| `image` | IMAGE | No | - | Imagen de referencia opcional para edición de imagen |
| `mask` | MASK | No | - | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) |
| `aspect_ratio` | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | La relación de aspecto para la generación de imagen. Se ignora si la resolución no está configurada en Auto (valor por defecto: "1:1") |
| `resolution` | COMBO | No | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La resolución para la generación de imagen. Si no está configurada en Auto, esto anula la configuración de aspect_ratio (valor por defecto: "Auto") |
| `magic_prompt_option` | COMBO | No | "AUTO"<br>"ON"<br>"OFF" | Determina si se debe usar MagicPrompt en la generación (valor por defecto: "AUTO") |
| `seed` | INT | No | 0-2147483647 | Semilla aleatoria para la generación (valor por defecto: 0) |
| `num_images` | INT | No | 1-8 | Número de imágenes a generar (valor por defecto: 1) |
| `rendering_speed` | COMBO | No | "DEFAULT"<br>"TURBO"<br>"QUALITY" | Controla la compensación entre velocidad de generación y calidad (valor por defecto: "DEFAULT") |
| `character_image` | IMAGE | No | - | Imagen para usar como referencia de personaje |
| `character_mask` | MASK | No | - | Máscara opcional para la imagen de referencia de personaje |

**Restricciones de Parámetros:**
- Cuando se proporcionan tanto `image` como `mask`, el nodo cambia al modo de edición
- Si solo se proporciona uno de `image` o `mask`, ocurrirá un error
- `character_mask` requiere que `character_image` esté presente
- El parámetro `aspect_ratio` se ignora cuando `resolution` no está configurado en "Auto"
- Las áreas blancas en la máscara serán reemplazadas durante el inpainting
- La máscara de personaje y la imagen de personaje deben tener el mismo tamaño

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La(s) imagen(es) generada(s) o editada(s) |