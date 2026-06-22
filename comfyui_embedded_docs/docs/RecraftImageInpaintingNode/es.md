# Recraft Relleno de Imagen

Este nodo modifica áreas específicas de una imagen basándose en un prompt de texto y una máscara. Utiliza la API de Recraft para editar inteligentemente solo las regiones enmascaradas, manteniendo el resto de la imagen sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se modificará | IMAGE | Sí | - |
| `mask` | La máscara que define qué áreas de la imagen deben modificarse | MASK | Sí | - |
| `prompt` | Prompt para la generación de la imagen (valor predeterminado: cadena vacía, longitud máxima: 1000 caracteres) | STRING | Sí | - |
| `n` | El número de imágenes a generar (valor predeterminado: 1, mínimo: 1, máximo: 6) | INT | Sí | 1-6 |
| `semilla` | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Parámetro de estilo opcional para la API de Recraft. Si no se proporciona, se usa el estilo "realistic_image" por defecto | STYLEV3 | No | - |
| `negative_prompt` | Una descripción textual opcional de elementos no deseados en una imagen (valor predeterminado: cadena vacía) | STRING | No | - |

*Nota: La `image` y la `mask` deben proporcionarse juntas para que la operación de inpainting funcione. La máscara se redimensionará automáticamente para coincidir con las dimensiones de la imagen. El `prompt` se valida y tiene una longitud máxima de 1000 caracteres.*

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La(s) imagen(es) modificada(s) generada(s) según el prompt y la máscara. Devuelve una imagen por cada imagen de entrada multiplicada por el parámetro `n` | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/es.md)

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
