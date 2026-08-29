# Recraft V4 Create Style

Este nodo crea un estilo Recraft V4 reutilizable a partir de 1 a 10 imágenes de referencia. El ID de estilo devuelto funciona con todos los modelos Recraft V4 y V4.1 del mismo tipo de salida y puede reutilizarse en pasos posteriores de generación de imágenes. El tamaño total de todas las imágenes de referencia está limitado a 10 MB.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Tipo de salida para el que se crea el estilo: recraftv4_styles para imágenes rasterizadas, recraftv4_styles_vector para SVG. | COMBO | Sí | "recraftv4_styles"<br>"recraftv4_styles_vector" |
| `images` | Imágenes de referencia que definen el estilo. Las referencias similares afinan la coincidencia; las referencias variadas la amplían. Ranura ampliable: conecte de 1 a 10 imágenes (`image_1` a `image_10`). | IMAGE | Sí | 1 a 10 imágenes |

### Notas

- Se requiere al menos una imagen de referencia; el nodo genera un error si no se proporciona ninguna.
- Se permite un máximo de 10 imágenes de referencia.
- El tamaño total codificado de todas las imágenes de referencia no debe superar los 10 MB; el nodo genera un error si se supera el límite.
- Cada imagen de referencia se reduce a un máximo de 2048×2048 píxeles y se codifica como WebP antes de enviarse a la API de Recraft.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `style_id` | Identificador único del estilo creado, utilizable con todos los modelos Recraft V4 y V4.1 del mismo tipo de salida. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/es.md)

---
**Source fingerprint (SHA-256):** `63b31ff08d5cfe7c0d4de6987f2ee5a34bd491237ed0fb4c93c225e33b7cede3`
