# Reve Mezclar Imagen

El nodo Reve Image Remix utiliza la API de Reve para generar una nueva imagen. Combina una o más imágenes de referencia con un prompt de texto para crear una nueva imagen remezclada a partir de la descripción proporcionada. Hay dos versiones de modelo disponibles y se puede aplicar un posprocesamiento opcional, como escalado o eliminación del fondo.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | Versión del modelo que se usará para la remezcla. Al seleccionar un modelo, se muestran sus ajustes de relación de aspecto y de escalado en tiempo de prueba. | DYNAMIC_COMBO | Sí | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `prompt` | Descripción de texto de la imagen deseada. Puede incluir etiquetas XML `img` para hacer referencia a imágenes específicas por índice, p. ej. `<img>0</img>`, `<img>1</img>`, etc. (por defecto: vacío) | STRING | Sí | de 1 a 2560 caracteres |
| `upscale` | Amplía la imagen generada. Puede añadir un costo adicional. Cuando se establece en "enabled", se muestra un ajuste `upscale_factor`. (por defecto: "disabled") | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Elimina el fondo de la imagen generada. Puede añadir un costo adicional. (por defecto: false) | BOOLEAN | No | `true`<br>`false` |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. (por defecto: 0) | INT | No | de 0 a 2147483647 |

### Entradas de la versión del modelo (compartidas por `reve-remix@20250915` y `reve-remix-fast@20251030`)

Ambas versiones del modelo exponen los mismos ajustes.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Relación de aspecto de la imagen de salida. Cuando se establece en "auto", la API decide la relación de aspecto automáticamente. | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Los valores más altos producen mejores imágenes, pero consumen más créditos. (por defecto: 1; solo se aplican valores mayores que 1) | INT | No | de 1 a 5 (paso 1) |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Ranura ampliable: conecta de 1 a 6 imágenes de referencia para usarlas como base para la remezcla (las ranuras se denominan `image_1`, `image_2`, etc.). Se requiere al menos una imagen de referencia. | IMAGE | Sí | de 1 a 6 imágenes |

**Nota:** El prompt debe tener entre 1 y 2560 caracteres. Cuando `upscale` se establece en "enabled", el ajuste anidado `upscale_factor` acepta 2, 3 o 4 (por defecto: 2) y puede añadir un costo adicional. Eliminar el fondo también puede añadir un costo adicional.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La nueva imagen generada por el proceso de remezcla de Reve. | IMAGE |

Nota: Este nodo está marcado como obsoleto.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/es.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
