# Recraft Imagen a Imagen

Este nodo modifica una imagen existente a partir de una indicación de texto y del parámetro `strength`. Utiliza la API de Recraft para transformar la imagen de entrada según la descripción proporcionada, manteniendo cierto grado de similitud con la imagen original en función del valor de `strength`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La imagen de entrada que se va a modificar. | IMAGE | Sí | - |
| `prompt` | Indicación para la generación de la imagen (por defecto: "", longitud máxima: 1000 caracteres). | STRING | Sí | - |
| `n` | El número de imágenes a generar (por defecto: 1). | INT | Sí | 1-6 |
| `strength` | Define la diferencia con la imagen original; debe estar en el intervalo [0, 1], donde 0 significa casi idéntica y 1 significa una similitud muy escasa (por defecto: 0.5). | FLOAT | Sí | 0.0-1.0 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección de estilo opcional para la generación de la imagen. Si no se proporciona, se utiliza el estilo `realistic_image` por defecto. | STYLEV3 | No | - |
| `negative_prompt` | Descripción de texto opcional de los elementos no deseados en una imagen (por defecto: ""). | STRING | No | - |
| `recraft_controls` | Controles adicionales opcionales sobre la generación mediante el nodo Recraft Controls. | CONTROLS | No | - |

**Nota:** El parámetro `seed` solo hace que el nodo se vuelva a ejecutar, pero no garantiza resultados deterministas. El valor de `strength` se redondea internamente a 2 decimales. La indicación se valida y no debe superar los 1000 caracteres. Si no se proporciona `recraft_style`, el nodo usa por defecto el estilo `realistic_image`. Si se utiliza un `style_id` de Infinite Style Library, asegúrese de que no sea un estilo de arte vectorial, ya que esto puede hacer que el nodo reciba datos SVG en lugar de una imagen, lo que provocaría un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La(s) imagen(es) generada(s) a partir de la imagen de entrada y de la indicación. Para cada imagen de entrada se generan `n` imágenes, por lo que el número total de salidas es igual al número de entradas multiplicado por `n`. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
