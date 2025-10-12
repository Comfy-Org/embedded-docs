> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/es.md)

El nodo CLIPTextEncodeSD3 procesa entradas de texto para modelos Stable Diffusion 3 mediante la codificación de múltiples prompts de texto utilizando diferentes modelos CLIP. Maneja tres entradas de texto separadas (clip_g, clip_l y t5xxl) y proporciona opciones para gestionar el relleno de texto vacío. El nodo asegura una alineación adecuada de tokens entre las diferentes entradas de texto y devuelve datos de acondicionamiento adecuados para las pipelines de generación de SD3.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Requerido | - | - | El modelo CLIP utilizado para la codificación de texto |
| `clip_l` | STRING | Multilínea, Prompts Dinámicos | - | - | Entrada de texto para el modelo CLIP local |
| `clip_g` | STRING | Multilínea, Prompts Dinámicos | - | - | Entrada de texto para el modelo CLIP global |
| `t5xxl` | STRING | Multilínea, Prompts Dinámicos | - | - | Entrada de texto para el modelo T5-XXL |
| `empty_padding` | COMBO | Selección | - | ["none", "empty_prompt"] | Controla cómo se manejan las entradas de texto vacías |

**Restricciones de Parámetros:**

- Cuando `empty_padding` se establece en "none", las entradas de texto vacías para `clip_g`, `clip_l` o `t5xxl` resultarán en listas de tokens vacías en lugar de relleno
- El nodo automáticamente equilibra las longitudes de tokens entre las entradas `clip_l` y `clip_g` rellenando la más corta con tokens vacíos cuando las longitudes difieren
- Todas las entradas de texto admiten prompts dinámicos y entrada de texto multilínea

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de acondicionamiento de texto codificados listos para usar en las pipelines de generación de SD3 |
