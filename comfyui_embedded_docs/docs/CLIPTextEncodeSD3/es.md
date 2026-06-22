# CLIPTextEncodeSD3

El nodo CLIPTextEncodeSD3 procesa entradas de texto para modelos Stable Diffusion 3 codificando múltiples indicaciones de texto utilizando diferentes modelos CLIP. Maneja tres entradas de texto separadas (`clip_g`, `clip_l` y `t5xxl`) y ofrece opciones para gestionar el relleno de texto vacío. El nodo asegura una alineación adecuada de tokens entre las diferentes entradas de texto y devuelve datos de condicionamiento adecuados para los flujos de generación SD3.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la codificación de texto | CLIP | Sí | - |
| `clip_l` | Entrada de texto para el modelo CLIP local. Admite texto multilínea e indicaciones dinámicas. | STRING | Sí | - |
| `clip_g` | Entrada de texto para el modelo CLIP global. Admite texto multilínea e indicaciones dinámicas. | STRING | Sí | - |
| `t5xxl` | Entrada de texto para el modelo T5-XXL. Admite texto multilínea e indicaciones dinámicas. | STRING | Sí | - |
| `empty_padding` | Controla cómo se manejan las entradas de texto vacías. Cuando se establece en "none", las entradas de texto vacías para `clip_g`, `clip_l` o `t5xxl` resultarán en listas de tokens vacías en lugar de relleno. Este es un parámetro avanzado (valor predeterminado: "none"). | COMBO | Sí | `"none"`<br>`"empty_prompt"` |

**Restricciones de parámetros:**

- Cuando `empty_padding` está configurado en "none", las entradas de texto vacías para `clip_g`, `clip_l` o `t5xxl` resultarán en listas de tokens vacías en lugar de relleno
- El nodo equilibra automáticamente las longitudes de tokens entre las entradas `clip_l` y `clip_g` rellenando la más corta con tokens vacíos cuando las longitudes difieren
- Todas las entradas de texto admiten indicaciones dinámicas y entrada de texto multilínea

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento de texto codificados listos para usar en flujos de generación SD3 | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/es.md)

---
**Source fingerprint (SHA-256):** `38f7538d05fe48e74f41f265550b83906b2f0c5d31f0783f6859f4df7b5cb9d3`
