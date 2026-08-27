# OpenAI DALL·E 2

Genera imágenes de forma síncrona a través del endpoint de DALL·E 2 de OpenAI.

## Cómo funciona

Este nodo se conecta a la API de DALL·E 2 de OpenAI para crear imágenes basadas en descripciones de texto. Cuando proporcionas un prompt de texto, el nodo lo envía a los servidores de OpenAI, que generan las imágenes correspondientes y las devuelven a ComfyUI. El nodo puede operar en dos modos: generación estándar de imágenes usando solo un prompt de texto, o modo de edición de imágenes cuando se proporcionan tanto una imagen como una máscara. En el modo de edición, usa la máscara para determinar qué partes de la imagen original deben modificarse mientras se mantienen sin cambios las demás áreas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para DALL·E (predeterminado: vacío) | STRING | Sí | - |
| `seed` | aún no implementado en el backend (predeterminado: 0) | INT | No | 0 a 2147483647 |
| `tamaño` | Tamaño de la imagen (predeterminado: "1024x1024") | COMBO | No | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Cuántas imágenes generar (predeterminado: 1) | INT | No | 1 a 8 |
| `imagen` | Imagen de referencia opcional para edición de imágenes. | IMAGE | No | - |
| `mask` | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) | MASK | No | - |

**Nota:** El modo de edición de imágenes se activa solo cuando se proporcionan tanto `image` como `mask` juntos. Si solo se suministra uno de ellos, se genera un error. La `mask` debe tener el mismo tamaño que la `image`; de lo contrario, se genera un error. En el modo de edición, las áreas blancas de la máscara indican las regiones que serán reemplazadas.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `IMAGE` | La(s) imagen(es) generada(s) o editada(s) de DALL·E 2 | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/es.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
