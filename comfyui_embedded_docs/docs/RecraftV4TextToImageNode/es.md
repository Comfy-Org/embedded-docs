# Recraft V4 Texto a Imagen

Este nodo genera imágenes a partir de descripciones de texto utilizando los modelos de IA Recraft V4 y V4.1. Envía tu prompt a una API externa y devuelve las imágenes generadas. Puedes controlar la salida especificando el modelo, el tamaño de la imagen, el número de imágenes y un estilo opcional, ya sea como ID de estilo guardado o a partir de imágenes de referencia.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo a utilizar para la generación. Los modelos recraftv4_styles están diseñados para la generación coherente con el estilo y siempre requieren un style_id o style_references. | DYNAMIC_COMBO | Sí | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt para la generación de la imagen. Máximo 10 000 caracteres. | STRING | Sí | 1 a 10000 characters |
| `prompt_negativo` | Esta entrada se ignora: el prompt negativo no es compatible con los modelos Recraft V4 y V4.1. | STRING | Sí | N/A |
| `n` | El número de imágenes a generar (predeterminado: 1). | INT | Sí | 1 a 6 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionales opcionales sobre la generación mediante el nodo Recraft Controls. | CUSTOM | No | N/A |
| `style_id` | UUID de un estilo de Recraft V4 a aplicar, p. ej. del nodo Recraft V4 Create Style o de la salida style_id de una ejecución anterior. No se puede combinar con style_references (predeterminado: vacío). | STRING | No | Valid UUID string |
| `style_match` | Qué fielmente seguir el estilo: precise lo reproduce en detalle, flexible coincide con el aspecto general. Solo se utiliza cuando se proporciona un estilo (predeterminado: "precise"). | COMBO | No | "precise"<br>"flexible" |

### Entradas de recraftv4_1, recraftv4_1_utility, recraftv4 y recraftv4_styles

Estos modelos comparten el mismo parámetro `size`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `size` | El tamaño de la imagen generada (predeterminado: "1024x1024"). | COMBO | Sí | Multiple options available (standard Recraft V4 sizes, includes "1024x1024") |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro y recraftv4_styles_pro

Estos modelos comparten el mismo parámetro `size`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `size` | El tamaño de la imagen generada (predeterminado: "2048x2048"). | COMBO | Sí | Multiple options available (pro Recraft V4 sizes, includes "2048x2048") |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `style_references` | Imágenes de referencia para crear un estilo sobre la marcha, facturadas además de la generación. El estilo creado se devuelve como style_id para reutilizarlo. No se puede combinar con style_id. Ranura ampliable: conecta de 1 a N imágenes (style_reference_1, style_reference_2, ...). | IMAGE | No | 0 hasta el número máximo de imágenes de referencia permitidas por la API de Recraft; el tamaño total codificado no debe superar los 10 MB |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. Los modelos `recraftv4_styles` y `recraftv4_styles_pro` siempre requieren un estilo: conecta imágenes de referencia de estilo o proporciona un `style_id`. Las entradas `style_id` y `style_references` son mutuamente excluyentes: proporciona solo una de ellas. Un `style_id` debe ser un UUID válido. La entrada `style_match` solo se usa cuando se proporciona un estilo. Las imágenes de referencia de estilo se facturan además de la generación y su tamaño total codificado no debe superar los 10 MB. El valor de `seed` no garantiza resultados de imagen reproducibles. Si usas un ID de estilo de Infinite Style Library, asegúrate de que no sea un estilo de arte vectorial, ya que esto puede devolver datos SVG en lugar de una imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La imagen generada o lote de imágenes. | IMAGE |
| `style_id` | El ID de estilo utilizado o creado por esta generación. Cuando se proporcionan imágenes de referencia de estilo, el estilo creado se devuelve aquí para su reutilización; cadena vacía cuando no se utiliza ningún estilo. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`
