# OpenAI DALL·E 3

Genera imágenes de forma síncrona a través del endpoint DALL·E 3 de OpenAI. Este nodo toma un prompt de texto y crea imágenes correspondientes utilizando el modelo DALL·E 3 de OpenAI, permitiéndote especificar la calidad, el estilo y las dimensiones de la imagen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para DALL·E (predeterminado: "") | STRING | Sí | - |
| `seed` | Aún no implementado en el backend (predeterminado: 0) | INT | No | 0 a 2147483647 |
| `calidad` | Calidad de la imagen (predeterminado: "standard") | COMBO | No | "standard"<br>"hd" |
| `estilo` | "Vivid" hace que el modelo se incline hacia la generación de imágenes hiperrealistas y dramáticas. "Natural" hace que el modelo produzca imágenes más naturales y menos hiperrealistas. (predeterminado: "natural") | COMBO | No | "natural"<br>"vivid" |
| `tamaño` | Tamaño de la imagen (predeterminado: "1024x1024") | COMBO | No | "1024x1024"<br>"1024x1792"<br>"1792x1024" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La imagen generada por DALL·E 3 | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/es.md)

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
