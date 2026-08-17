# OpenAI DALL·E 2

OpenAI DALL·E 2 genera imágenes de forma síncrona mediante el endpoint de OpenAI DALL·E 2. Proporciona un prompt de texto para crear nuevas imágenes, o proporciona tanto una imagen como una máscara para editar una imagen existente.

## Cómo funciona

Este nodo se conecta a la API de OpenAI DALL·E 2 para crear imágenes basadas en descripciones de texto. Cuando proporcionas un prompt de texto, el nodo lo envía a los servidores de OpenAI, que generan las imágenes correspondientes y las devuelven a ComfyUI. El nodo puede funcionar en dos modos: generación estándar de imágenes usando solo un prompt de texto, o modo de edición de imágenes cuando se proporcionan tanto una imagen como una máscara. En el modo de edición, usa la máscara para determinar qué partes de la imagen original deben modificarse mientras mantiene intactas otras áreas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto para DALL·E (por defecto: vacío) | STRING | Sí | - |
| `seed` | aún no implementado en el backend (por defecto: 0) | INT | No | 0 a 2147483647 |
| `size` | Tamaño de la imagen (por defecto: "1024x1024") | COMBO | No | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Cuántas imágenes generar (por defecto: 1) | INT | No | 1 a 8 |
| `image` | Imagen de referencia opcional para la edición de imágenes. | IMAGE | No | - |
| `mask` | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) | MASK | No | - |

Nota: `image` y `mask` deben proporcionarse juntas. Cuando se proporcionan ambas, el nodo cambia al modo de edición de imágenes. Si solo se proporciona una de ellas, se genera un error. La `mask` debe tener el mismo tamaño que la `image`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La(s) imagen(es) generada(s) o editada(s) de DALL·E 2 | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/es.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
