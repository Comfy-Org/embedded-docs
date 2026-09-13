# OpenAIDalle2

Genera imágenes de forma sincrónica a través del endpoint DALL·E 2 de OpenAI. El nodo envía un prompt de texto a la API DALL·E 2 de OpenAI y devuelve la(s) imagen(es) resultante(s) a ComfyUI. También puede editar una imagen existente cuando se proporcionan juntos una `image` y una `mask`.

## Cómo funciona

Este nodo se conecta a la API DALL·E 2 de OpenAI para crear imágenes basadas en descripciones de texto. Cuando proporcionas un prompt de texto, el nodo lo envía a los servidores de OpenAI, que generan las imágenes correspondientes y las devuelven a ComfyUI. El nodo puede funcionar en dos modos: generación estándar de imágenes usando solo un prompt de texto, o modo de edición de imágenes cuando se proporcionan tanto una imagen como una máscara. En el modo de edición, utiliza la máscara para determinar qué partes de la imagen original deben modificarse mientras mantiene sin cambios otras áreas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para DALL·E (predeterminado: vacío) | STRING | Sí | - |
| `seed` | Aún no implementado en el backend (predeterminado: 0) | INT | No | 0 a 2147483647 |
| `size` | Tamaño de la imagen (predeterminado: "1024x1024") | COMBO | No | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Cuántas imágenes generar (predeterminado: 1) | INT | No | 1 a 8 |
| `image` | Imagen de referencia opcional para la edición de imágenes. | IMAGE | No | - |
| `mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán) | MASK | No | - |

**Nota:** El modo de edición de imágenes se activa solo cuando se proporcionan juntos `image` y `mask`. Si solo se proporciona uno de ellos, se genera un error. La `mask` debe tener el mismo tamaño que la `image`; de lo contrario, se genera un error. En el modo de edición, las áreas blancas de la máscara indican las regiones que serán reemplazadas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | La(s) imagen(es) generada(s) o editada(s) por DALL·E 2 | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/es.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
