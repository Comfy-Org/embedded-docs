# Recraft Relleno de Imagen

Este nodo modifica áreas específicas de una imagen basándose en un prompt de texto y una máscara. Utiliza la API de Recraft para editar de forma inteligente solo las regiones enmascaradas, manteniendo el resto de la imagen sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | La imagen de entrada que se va a modificar | IMAGE | Sí | - |
| `mask` | La máscara que define qué áreas de la imagen deben modificarse | MASK | Sí | - |
| `prompt` | Prompt para la generación de la imagen (valor predeterminado: cadena vacía, longitud máxima: 1000 caracteres) | STRING | Sí | - |
| `n` | El número de imágenes a generar (valor predeterminado: 1, mínimo: 1, máximo: 6) | INT | Sí | 1-6 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Parámetro de estilo opcional para la API de Recraft. Si no se proporciona, el valor predeterminado es el estilo `realistic_image` | STYLEV3 | No | - |
| `negative_prompt` | Una descripción de texto opcional de los elementos no deseados en una imagen (valor predeterminado: cadena vacía) | STRING | No | - |

*Nota: `image` y `mask` deben proporcionarse juntas para que la operación de inpainting funcione. La máscara se redimensionará automáticamente para coincidir con las dimensiones de la imagen. El `prompt` se valida y tiene una longitud máxima de 1000 caracteres. Si se utiliza un `style_id` de la Infinite Style Library, asegúrate de que no sea un estilo de arte vectorial, ya que esto puede hacer que la API devuelva datos SVG en lugar de una imagen.*

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La(s) imagen(es) modificada(s) generada(s) a partir del prompt y la máscara. Devuelve una imagen por cada imagen de entrada multiplicada por el parámetro `n` | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/es.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
