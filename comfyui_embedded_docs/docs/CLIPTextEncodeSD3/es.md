# CLIPTextEncodeSD3

El nodo CLIPTextEncodeSD3 procesa las entradas de texto para los modelos Stable Diffusion 3 codificando múltiples prompts de texto mediante diferentes modelos CLIP. Maneja tres entradas de texto separadas (`clip_g`, `clip_l` y `t5xxl`) y ofrece opciones para gestionar el relleno de texto vacío. El nodo garantiza una alineación adecuada de tokens entre las distintas entradas de texto y devuelve datos de condicionamiento adecuados para los pipelines de generación SD3.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip` | El modelo CLIP utilizado para la codificación de texto | CLIP | Sí | - |
| `clip_l` | Entrada de texto para el modelo CLIP local. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `clip_g` | Entrada de texto para el modelo CLIP global. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `t5xxl` | Entrada de texto para el modelo T5-XXL. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |
| `empty_padding` | Controla cómo se manejan las entradas de texto vacías. Cuando se establece en "none", las entradas de texto vacías para `clip_g`, `clip_l` o `t5xxl` darán como resultado listas de tokens vacías en lugar de relleno. Este es un parámetro avanzado (valor predeterminado: "none"). | COMBO | Sí | `"none"`<br>`"empty_prompt"` |

**Restricciones de parámetros:**

- Cuando `empty_padding` se establece en "none", las entradas de texto vacías para `clip_g`, `clip_l` o `t5xxl` darán como resultado listas de tokens vacías en lugar de relleno.
- El nodo equilibra automáticamente las longitudes de tokens entre las entradas `clip_l` y `clip_g` rellenando la más corta con tokens vacíos cuando las longitudes difieren.
- Todas las entradas de texto admiten prompts dinámicos y entrada de texto multilínea.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `CONDITIONING` | Los datos de condicionamiento de texto codificados, listos para usarse en pipelines de generación SD3 | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/es.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`
