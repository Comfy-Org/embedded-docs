> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/es.md)

Genera imágenes de forma síncrona a través del endpoint DALL·E 3 de OpenAI. Este nodo toma un prompt de texto y crea imágenes correspondientes utilizando el modelo DALL·E 3 de OpenAI, permitiéndote especificar la calidad, el estilo y las dimensiones de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt de texto para DALL·E (predeterminado: "") |
| `seed` | INT | No | 0 a 2147483647 | Aún no implementado en el backend (predeterminado: 0) |
| `quality` | COMBO | No | "standard"<br>"hd" | Calidad de la imagen (predeterminado: "standard") |
| `style` | COMBO | No | "natural"<br>"vivid" | "Vivid" hace que el modelo se incline hacia la generación de imágenes hiperrealistas y dramáticas. "Natural" hace que el modelo produzca imágenes más naturales y menos hiperrealistas. (predeterminado: "natural") |
| `size` | COMBO | No | "1024x1024"<br>"1024x1792"<br>"1792x1024" | Tamaño de la imagen (predeterminado: "1024x1024") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La imagen generada por DALL·E 3 |

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
