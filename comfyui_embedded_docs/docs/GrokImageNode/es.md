# Imagen Grok

El nodo Grok Image genera una o más imágenes basadas en un prompt de texto utilizando los modelos de imagen de Grok AI. Envía el prompt y la configuración a un servicio externo y devuelve las imágenes generadas como tensores que pueden utilizarse en otras partes del flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo Grok específico a utilizar para la generación de imágenes. Los diferentes modelos pueden ofrecer calidad, velocidad o características variables. | COMBO | Sí | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | El prompt de texto utilizado para generar la imagen. Esta descripción guía a la IA sobre qué crear. Debe contener al menos 1 carácter que no sea un espacio en blanco. | STRING | Sí | N/A |
| `aspect_ratio` | La relación ancho-alto deseada para la imagen generada. | COMBO | Sí | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | Número de imágenes a generar (por defecto: 1). | INT | Sí | 1 a 10 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 2147483647 |
| `resolution` | La resolución de salida deseada para las imágenes generadas (por defecto: "1K"). | COMBO | No | `"1K"`<br>`"2K"` |
| `quality` | Nivel de calidad, compatible únicamente con el modelo grok-imagine-image-2.0 (por defecto: "medium"). | COMBO | No | Múltiples opciones disponibles |

**Nota:** El parámetro `quality` solo se aplica cuando `model` está establecido en "grok-imagine-image-2.0". Para todos los demás modelos, esta configuración se ignora.

**Nota:** El parámetro `seed` se utiliza principalmente para controlar cuándo el nodo se vuelve a ejecutar dentro de un flujo de trabajo. Debido a la naturaleza del servicio externo de IA, las imágenes generadas no son reproducibles entre ejecuciones, incluso con una semilla idéntica.

**Nota sobre precios:** El costo de generar imágenes depende del `model`, la `resolution`, la `quality` y el `number_of_images` seleccionados; el precio total es la tarifa por imagen multiplicada por `number_of_images`. Para el modelo "grok-imagine-image-2.0", la tarifa por imagen es de $0.04 en resolución "1K" y $0.06 en "2K" con calidad "low", o de $0.06 en "1K" y $0.08 en "2K" con otros niveles de calidad. El modelo "grok-imagine-image-quality" cuesta $0.05 por imagen en "1K" y $0.07 por imagen en "2K". El modelo "grok-imagine-image-pro" cuesta $0.07 por imagen. Otros modelos cuestan $0.02 por imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La imagen generada o un lote de imágenes. Si `number_of_images` es 1, se devuelve un único tensor de imagen. Si es mayor que 1, se devuelve un lote de tensores de imagen. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/es.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
