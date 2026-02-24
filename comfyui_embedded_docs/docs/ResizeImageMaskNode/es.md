> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/es.md)

El nodo Redimensionar Imagen/Máscara proporciona múltiples métodos para cambiar las dimensiones de una imagen o máscara de entrada. Puede escalar mediante un multiplicador, establecer dimensiones específicas, igualar el tamaño de otra entrada o ajustar basándose en el recuento de píxeles, utilizando varios métodos de interpolación para mantener la calidad.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE o MASK | Sí | N/A | La imagen o máscara que se va a redimensionar. |
| `resize_type` | COMBO | Sí | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | El método utilizado para determinar el nuevo tamaño. Los parámetros requeridos cambian según el tipo seleccionado. |
| `multiplier` | FLOAT | No | 0.01 a 8.0 | El factor de escala. Requerido cuando `resize_type` es `SCALE_BY` (por defecto: 1.00). |
| `width` | INT | No | 0 a 8192 | El ancho objetivo en píxeles. Requerido cuando `resize_type` es `SCALE_DIMENSIONS` o `SCALE_WIDTH` (por defecto: 512). |
| `height` | INT | No | 0 a 8192 | La altura objetivo en píxeles. Requerido cuando `resize_type` es `SCALE_DIMENSIONS` o `SCALE_HEIGHT` (por defecto: 512). |
| `crop` | COMBO | No | `"disabled"`<br>`"center"` | El método de recorte a aplicar cuando las dimensiones no coinciden con la relación de aspecto. Solo disponible cuando `resize_type` es `SCALE_DIMENSIONS` o `MATCH_SIZE` (por defecto: "center"). |
| `longer_size` | INT | No | 0 a 8192 | El tamaño objetivo para el lado más largo de la imagen. Requerido cuando `resize_type` es `SCALE_LONGER_DIMENSION` (por defecto: 512). |
| `shorter_size` | INT | No | 0 a 8192 | El tamaño objetivo para el lado más corto de la imagen. Requerido cuando `resize_type` es `SCALE_SHORTER_DIMENSION` (por defecto: 512). |
| `megapixels` | FLOAT | No | 0.01 a 16.0 | El número total objetivo de megapíxeles. Requerido cuando `resize_type` es `SCALE_TOTAL_PIXELS` (por defecto: 1.0). |
| `match` | IMAGE o MASK | No | N/A | Una imagen o máscara cuyas dimensiones se utilizarán para redimensionar la entrada. Requerido cuando `resize_type` es `MATCH_SIZE`. |
| `scale_method` | COMBO | Sí | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | El algoritmo de interpolación utilizado para el escalado (por defecto: "area"). |

**Nota:** El parámetro `crop` solo está disponible y es relevante cuando `resize_type` está configurado como `SCALE_DIMENSIONS` o `MATCH_SIZE`. Al usar `SCALE_WIDTH` o `SCALE_HEIGHT`, la otra dimensión se escala automáticamente para mantener la relación de aspecto original.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `resized` | IMAGE o MASK | La imagen o máscara redimensionada, que coincide con el tipo de dato de la entrada. |
