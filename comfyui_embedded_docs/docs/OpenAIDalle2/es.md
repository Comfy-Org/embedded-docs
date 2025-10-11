> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/es.md)

Genera imágenes de forma síncrona mediante el endpoint DALL·E 2 de OpenAI.

## Cómo Funciona

Este nodo se conecta a la API DALL·E 2 de OpenAI para crear imágenes basadas en descripciones de texto. Cuando se proporciona un texto descriptivo, el nodo lo envía a los servidores de OpenAI que generan las imágenes correspondientes y las devuelven a ComfyUI. El nodo puede operar en dos modos: generación estándar de imágenes usando solo un texto descriptivo, o modo de edición de imágenes cuando se proporcionan tanto una imagen como una máscara. En el modo de edición, utiliza la máscara para determinar qué partes de la imagen original deben modificarse manteniendo sin cambios otras áreas.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | requerido | "" | - | Texto descriptivo para DALL·E |
| `seed` | INT | opcional | 0 | 0 a 2147483647 | aún no implementado en el backend |
| `size` | COMBO | opcional | "1024x1024" | "256x256", "512x512", "1024x1024" | Tamaño de imagen |
| `n` | INT | opcional | 1 | 1 a 8 | Cuántas imágenes generar |
| `image` | IMAGE | opcional | None | - | Imagen de referencia opcional para edición de imagen. |
| `mask` | MASK | opcional | None | - | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) generada(s) o editada(s) desde DALL·E 2 |