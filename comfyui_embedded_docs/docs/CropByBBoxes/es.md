> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/es.md)

El nodo CropByBBoxes extrae y redimensiona regiones rectangulares específicas de un lote de imágenes de entrada. Utiliza las coordenadas de las cajas delimitadoras proporcionadas para definir el área a recortar de cada imagen. Las regiones recortadas se redimensionan luego a una dimensión de salida especificada, con opciones para estirar el recorte o rellenarlo para preservar su relación de aspecto original.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | El lote de imágenes de entrada para recortar. |
| `bboxes` | BOUNDINGBOX | Sí | - | La lista de cajas delimitadoras que definen las regiones a recortar. Esta entrada es forzada, lo que significa que debe estar conectada. |
| `output_width` | INT | No | 64 - 4096 | El ancho al que se redimensiona cada recorte (por defecto: 512). |
| `output_height` | INT | No | 64 - 4096 | La altura a la que se redimensiona cada recorte (por defecto: 512). |
| `padding` | INT | No | 0 - 1024 | Relleno extra en píxeles añadido a cada lado de la caja delimitadora antes de recortar (por defecto: 0). |
| `keep_aspect` | COMBO | No | `"stretch"`<br>`"pad"` | Si se debe estirar el recorte para ajustarse al tamaño de salida, o rellenar con píxeles negros para preservar su relación de aspecto (por defecto: "stretch"). |

**Nota:** El nodo procesa un fotograma de imagen a la vez. Si se proporcionan múltiples cajas delimitadoras para un solo fotograma, calcula una única región de recorte que es la unión (el rectángulo más pequeño que contiene todas las cajas) de todas las cajas proporcionadas. Si una región de recorte calculada no es válida (por ejemplo, ancho o altura cero), el nodo creará un recorte de respaldo desde la parte superior central de la imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | Todas las regiones recortadas y redimensionadas, apiladas en un único lote de imágenes. |