> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/es.md)

Este nodo modifica áreas específicas de una imagen basándose en un prompt de texto y una máscara. Utiliza la API de Recraft para editar inteligentemente solo las regiones enmascaradas, manteniendo el resto de la imagen sin cambios.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se modificará |
| `mask` | MASK | Sí | - | La máscara que define qué áreas de la imagen deben modificarse |
| `prompt` | STRING | Sí | - | Prompt para la generación de la imagen (valor predeterminado: cadena vacía, longitud máxima: 1000 caracteres) |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar (valor predeterminado: 1, mínimo: 1, máximo: 6) |
| `seed` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor predeterminado: 0) |
| `recraft_style` | STYLEV3 | No | - | Parámetro de estilo opcional para la API de Recraft. Si no se proporciona, se usa el estilo "realistic_image" por defecto |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen (valor predeterminado: cadena vacía) |

*Nota: La `image` y la `mask` deben proporcionarse juntas para que la operación de inpainting funcione. La máscara se redimensionará automáticamente para coincidir con las dimensiones de la imagen. El `prompt` se valida y tiene una longitud máxima de 1000 caracteres.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La(s) imagen(es) modificada(s) generada(s) según el prompt y la máscara. Devuelve una imagen por cada imagen de entrada multiplicada por el parámetro `n` |

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
