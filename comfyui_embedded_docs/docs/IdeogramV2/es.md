> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/es.md)

El nodo Ideogram V2 genera imágenes utilizando el modelo de IA Ideogram V2. Toma indicaciones de texto y varias configuraciones de generación para crear imágenes a través de un servicio API. El nodo admite diferentes relaciones de aspecto, resoluciones y opciones de estilo para personalizar las imágenes de salida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación para la generación de imágenes (valor por defecto: cadena vacía) |
| `turbo` | BOOLEAN | No | - | Si se debe utilizar el modo turbo (generación más rápida, potencialmente menor calidad) (valor por defecto: False) |
| `aspect_ratio` | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | La relación de aspecto para la generación de imágenes. Se ignora si la resolución no está establecida en AUTO. (valor por defecto: "1:1") |
| `resolution` | COMBO | No | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La resolución para la generación de imágenes. Si no está establecida en AUTO, esto anula la configuración de aspect_ratio. (valor por defecto: "Auto") |
| `magic_prompt_option` | COMBO | No | "AUTO"<br>"ON"<br>"OFF" | Determina si se debe usar MagicPrompt en la generación (valor por defecto: "AUTO") |
| `seed` | INT | No | 0-2147483647 | Semilla aleatoria para la generación (valor por defecto: 0) |
| `style_type` | COMBO | No | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | Tipo de estilo para la generación (solo V2) (valor por defecto: "NONE") |
| `negative_prompt` | STRING | No | - | Descripción de qué excluir de la imagen (valor por defecto: cadena vacía) |
| `num_images` | INT | No | 1-8 | Número de imágenes a generar (valor por defecto: 1) |

**Nota:** Cuando `resolution` no está establecida en "Auto", anula la configuración de `aspect_ratio`. El parámetro `num_images` tiene un límite máximo de 8 imágenes por generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La(s) imagen(es) generada(s) por el modelo Ideogram V2 |