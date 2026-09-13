# Recraft V4 Texto a Imagen

Genera imágenes a partir de prompts de texto usando los modelos Recraft V4 y V4.1. Envía el prompt y la configuración seleccionada a la API de Recraft y devuelve la imagen o las imágenes generadas. Si se usan imágenes de referencia de estilo, también se devuelve el ID de estilo creado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo que se usará para la generación. Los modelos recraftv4_styles están diseñados para una generación coherente en estilo y siempre requieren un style_id o style_references. | DYNAMIC_COMBO | Sí | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt para la generación de la imagen. Máximo 10.000 caracteres. | STRING | Sí | 1 a 10000 caracteres |
| `negative_prompt` | Esta entrada se ignora: los modelos Recraft V4 y V4.1 no admiten el prompt negativo. | STRING | Sí | N/A |
| `n` | El número de imágenes a generar (predeterminado: 1). | INT | Sí | 1 a 6 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales no son deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. | CUSTOM | No | N/A |
| `style_id` | UUID de un estilo de Recraft V4 que se aplicará, p. ej., desde el nodo Recraft V4 Create Style o la salida `style_id` de una ejecución anterior. No se puede combinar con style_references (predeterminado: vacío). | STRING | No | Cadena UUID válida |
| `style_match` | Qué tan fielmente se debe seguir el estilo: precise lo reproduce en detalle, flexible coincide con el aspecto general. Solo se usa cuando se proporciona un estilo (predeterminado: "precise"). | COMBO | No | "precise"<br>"flexible" |

### Entradas de recraftv4_1, recraftv4_1_utility, recraftv4 y recraftv4_styles

Estos modelos comparten el mismo parámetro `size`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `size` | El tamaño de la imagen generada (predeterminado: "1024x1024"). | COMBO | Sí | Varias opciones disponibles (tamaños estándar de Recraft V4; incluye "1024x1024") |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro y recraftv4_styles_pro

Estos modelos comparten el mismo parámetro `size`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `size` | El tamaño de la imagen generada (predeterminado: "2048x2048"). | COMBO | Sí | Varias opciones disponibles (tamaños pro de Recraft V4; incluye "2048x2048") |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Imágenes de referencia para crear un estilo sobre la marcha, facturadas además de la generación. El estilo creado se devuelve como style_id para reutilizarlo. No se puede combinar con style_id. Ranura ampliable: conecta 1..N imágenes (style_reference_1, style_reference_2, ...). | IMAGE | No | 0 hasta el número máximo de imágenes de referencia permitidas por la API de Recraft; el tamaño codificado total no debe superar los 10 MB |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. Los modelos `recraftv4_styles` y `recraftv4_styles_pro` siempre requieren un estilo: conecta imágenes de referencia de estilo o proporciona un `style_id`. Las entradas `style_id` y `style_references` son mutuamente excluyentes; proporciona solo una de ellas. Un `style_id` debe ser un UUID válido. La entrada `style_match` solo se usa cuando se proporciona un estilo. Las imágenes de referencia de estilo se facturan además de la generación y su tamaño codificado total no debe superar los 10 MB. El valor de `seed` no garantiza resultados de imagen reproducibles. Si usas un ID de estilo de la Infinite Style Library, asegúrate de que no sea un estilo de Vector art, ya que esto puede devolver datos SVG en lugar de una imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La imagen generada o el lote de imágenes. | IMAGE |
| `style_id` | El ID de estilo usado o creado por esta generación. Cuando se proporcionan imágenes de referencia de estilo, el estilo creado se devuelve aquí para reutilizarlo; cadena vacía cuando no se usa ningún estilo. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`
