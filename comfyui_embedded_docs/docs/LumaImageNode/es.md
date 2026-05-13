> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/es.md)

Genera imágenes de forma síncrona basándose en un texto de descripción y una relación de aspecto. Este nodo crea imágenes utilizando descripciones textuales y permite controlar las dimensiones y el estilo de la imagen a través de diversas entradas de referencia, incluyendo imágenes de personajes y de estilo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción para la generación de la imagen (valor predeterminado: cadena vacía). Debe tener al menos 3 caracteres de longitud. |
| `model` | COMBO | Sí | `photon-flash-1`<br>`photon-1`<br>`photon` | Selección del modelo para la generación de imágenes. Diferentes modelos tienen diferentes costos. |
| `aspect_ratio` | COMBO | Sí | `16:9`<br>`1:1`<br>`4:3`<br>`3:2`<br>`21:9`<br>`9:16`<br>`3:4`<br>`2:3`<br>`9:21` | Relación de aspecto para la imagen generada (valor predeterminado: `16:9`) |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor predeterminado: 0) |
| `style_image_weight` | FLOAT | No | 0.0 a 1.0 | Peso de la imagen de estilo. Se ignora si no se proporciona `style_image` (valor predeterminado: 1.0) |
| `image_luma_ref` | LUMA_REF | No | - | Conexión del nodo de referencia Luma para influir en la generación con imágenes de entrada; se pueden considerar hasta 4 imágenes. |
| `style_image` | IMAGE | No | - | Imagen de referencia de estilo; solo se utilizará 1 imagen. |
| `character_image` | IMAGE | No | - | Imágenes de referencia de personaje; puede ser un lote de varias, se pueden considerar hasta 4 imágenes. |

**Restricciones de los parámetros:**

- El `prompt` debe tener al menos 3 caracteres de longitud después de eliminar los espacios en blanco.
- El parámetro `image_luma_ref` puede aceptar hasta 4 imágenes de referencia.
- El parámetro `character_image` puede aceptar hasta 4 imágenes de referencia de personaje.
- El parámetro `style_image` acepta solo 1 imagen de referencia de estilo.
- El parámetro `style_image_weight` solo se utiliza cuando se proporciona `style_image`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | La imagen generada basada en los parámetros de entrada. |

---
**Source fingerprint (SHA-256):** `f7878cd4df62c2f364e4e404215b18bf2f5745fb071ae2cd931d5e34b84eab46`
