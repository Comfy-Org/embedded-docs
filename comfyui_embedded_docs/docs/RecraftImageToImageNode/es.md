# Recraft Imagen a Imagen

Este nodo modifica una imagen existente basándose en un texto de instrucción y un parámetro de intensidad. Utiliza la API de Recraft para transformar la imagen de entrada según la descripción proporcionada, manteniendo cierto grado de similitud con la imagen original en función del valor de intensidad.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se va a modificar | IMAGE | Sí | - |
| `prompt` | Instrucción para la generación de la imagen (valor predeterminado: "", longitud máxima: 1000 caracteres) | STRING | Sí | - |
| `n` | El número de imágenes a generar (valor predeterminado: 1) | INT | Sí | 1-6 |
| `intensidad` | Define la diferencia con la imagen original; debe estar en [0, 1], donde 0 significa casi idéntica y 1 significa similitud mínima (valor predeterminado: 0.5) | FLOAT | Sí | 0.0-1.0 |
| `semilla` | Semilla para determinar si el nodo debe reejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección opcional de estilo para la generación de la imagen. Si no se proporciona, se utiliza por defecto `realistic_image` | STYLEV3 | No | - |
| `negative_prompt` | Una descripción textual opcional de elementos no deseados en la imagen (valor predeterminado: "") | STRING | No | - |
| `recraft_controls` | Controles adicionales opcionales sobre la generación a través del nodo Controles Recraft | CONTROLS | No | - |

**Nota:** El parámetro `seed` solo desencadena la reejecución del nodo, pero no garantiza resultados deterministas. El parámetro de intensidad se redondea internamente a 2 decimales. La instrucción se valida y no debe superar los 1000 caracteres. Si no se proporciona `recraft_style`, el nodo utiliza por defecto el estilo `realistic_image`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La(s) imagen(es) generada(s) basada(s) en la imagen de entrada y la instrucción | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`
