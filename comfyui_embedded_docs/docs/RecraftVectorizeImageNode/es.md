# Recraft vectorizar imagen

Genera gráficos vectoriales SVG a partir de una imagen de entrada. Este nodo convierte imágenes raster en formato vectorial escalable enviando cada imagen a la API de Recraft y combinando los resultados en una única salida SVG.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `imagen` | La imagen de entrada que se va a convertir al formato SVG. Admite el procesamiento por lotes de varias imágenes. | IMAGE | Sí | - |
| `version` | La versión del vectorizador: `v1` es la versión estándar, y `v1_pro` (Vectorizer Pro) proporciona SVG más limpios con curvas suaves, líneas rectas y esquinas definidas, ideal para rotulación y formas intrincadas (predeterminado: "v1"). | COMBO | No | "v1"<br>"v1_pro" |
| `shape_stacking` | Cómo se apilan las formas en el SVG: `hierarchical` apila las formas unas sobre otras; `cut_out` crea formas que nunca se superponen, para plóters, cortadoras de vinilo y serigrafía (predeterminado: "hierarchical"). | COMBO | No | "hierarchical"<br>"cut_out" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `SVG` | La salida de gráficos vectoriales generada que combina todas las imágenes procesadas en un único documento SVG. | SVG |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/es.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
