> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/es.md)

El nodo IdeogramV1 genera imágenes utilizando el modelo Ideogram V1 a través de una API. Toma indicaciones de texto y varias configuraciones de generación para crear una o más imágenes basadas en su entrada. El nodo admite diferentes relaciones de aspecto y modos de generación para personalizar la salida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación para la generación de imágenes (valor por defecto: vacío) |
| `turbo` | BOOLEAN | Sí | - | Si se debe utilizar el modo turbo (generación más rápida, potencialmente menor calidad) (valor por defecto: False) |
| `aspect_ratio` | COMBO | No | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | La relación de aspecto para la generación de imágenes (valor por defecto: "1:1") |
| `magic_prompt_option` | COMBO | No | "AUTO"<br>"ON"<br>"OFF" | Determina si se debe usar MagicPrompt en la generación (valor por defecto: "AUTO") |
| `seed` | INT | No | 0-2147483647 | Valor de semilla aleatoria para la generación (valor por defecto: 0) |
| `negative_prompt` | STRING | No | - | Descripción de qué excluir de la imagen (valor por defecto: vacío) |
| `num_images` | INT | No | 1-8 | Número de imágenes a generar (valor por defecto: 1) |

**Nota:** El parámetro `num_images` tiene un límite máximo de 8 imágenes por solicitud de generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La(s) imagen(es) generada(s) por el modelo Ideogram V1 |