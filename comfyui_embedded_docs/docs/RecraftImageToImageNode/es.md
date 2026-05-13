> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/es.md)

Este nodo modifica una imagen existente basándose en un texto de instrucción y un parámetro de intensidad. Utiliza la API de Recraft para transformar la imagen de entrada según la descripción proporcionada, manteniendo cierto grado de similitud con la imagen original en función del valor de intensidad.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a modificar |
| `prompt` | STRING | Sí | - | Instrucción para la generación de la imagen (valor predeterminado: "", longitud máxima: 1000 caracteres) |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar (valor predeterminado: 1) |
| `strength` | FLOAT | Sí | 0.0-1.0 | Define la diferencia con la imagen original; debe estar en [0, 1], donde 0 significa casi idéntica y 1 significa similitud mínima (valor predeterminado: 0.5) |
| `seed` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe reejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor predeterminado: 0) |
| `recraft_style` | STYLEV3 | No | - | Selección opcional de estilo para la generación de la imagen. Si no se proporciona, se utiliza por defecto `realistic_image` |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en la imagen (valor predeterminado: "") |
| `recraft_controls` | CONTROLS | No | - | Controles adicionales opcionales sobre la generación a través del nodo Controles Recraft |

**Nota:** El parámetro `seed` solo desencadena la reejecución del nodo, pero no garantiza resultados deterministas. El parámetro de intensidad se redondea internamente a 2 decimales. La instrucción se valida y no debe superar los 1000 caracteres. Si no se proporciona `recraft_style`, el nodo utiliza por defecto el estilo `realistic_image`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La(s) imagen(es) generada(s) basada(s) en la imagen de entrada y la instrucción |

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`
