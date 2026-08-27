# Recraft Imagen a Imagen

Este nodo modifica una imagen existente basándose en un prompt de texto y un parámetro de intensidad. Utiliza la API de Recraft V3 para transformar la imagen de entrada según la descripción proporcionada, manteniendo cierto parecido con la imagen original, controlado por el ajuste de intensidad.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | La imagen de entrada que se va a modificar | IMAGE | Sí | - |
| `prompt` | Prompt para la generación de la imagen (predeterminado: cadena vacía, longitud máxima: 1000 caracteres) | STRING | Sí | - |
| `n` | El número de imágenes a generar (predeterminado: 1) | INT | Sí | 1-6 |
| `intensidad` | Define la diferencia con la imagen original; debe estar en [0, 1], donde 0 significa casi idéntica y 1 significa mínima similitud (predeterminado: 0.5) | FLOAT | Sí | 0.0-1.0 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección opcional de estilo para la generación de la imagen. Si no se proporciona, se usa `realistic_image` por defecto | STYLEV3 | No | - |
| `negative_prompt` | Una descripción de texto opcional de elementos no deseados en una imagen (predeterminado: cadena vacía) | STRING | No | - |
| `recraft_controls` | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls | CONTROLS | No | - |

**Nota:** El parámetro `seed` solo provoca la re-ejecución del nodo, pero no garantiza resultados deterministas. El parámetro `strength` se redondea a 2 decimales internamente. El parámetro `prompt` se valida y no debe exceder los 1000 caracteres. Un `negative_prompt` vacío se trata como ausencia de prompt negativo. Si no se proporciona `recraft_style`, el nodo usa el estilo `realistic_image` por defecto. Si usas un `style_id` de la Infinite Style Library, asegúrate de que no sea un estilo de arte vectorial, ya que esto puede hacer que el nodo reciba datos SVG en lugar de una imagen, lo que resultará en un error. Cuando la `image` de entrada es un lote, cada imagen del lote se procesa individualmente y todos los resultados se devuelven juntos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La(s) imagen(es) generada(s) a partir de la imagen de entrada y el prompt | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
