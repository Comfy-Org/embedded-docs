> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/es.md)

El nodo Redimensionar Imagen/Máscara proporciona múltiples métodos para cambiar las dimensiones de una imagen o máscara de entrada. Puede escalar mediante un multiplicador, establecer dimensiones específicas, igualar el tamaño de otra entrada o ajustarse según la cantidad de píxeles, utilizando diversos métodos de interpolación para garantizar la calidad.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `input` | IMAGE o MASK | Sí | N/A | La imagen o máscara que se va a redimensionar. |
| `resize_type` | COMBO | Sí | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | El método utilizado para determinar el nuevo tamaño. Los parámetros requeridos cambian según el tipo seleccionado. |
| `multiplier` | FLOAT | No | 0.01 a 8.0 | El factor de escala. Obligatorio cuando `resize_type` es `SCALE_BY` (predeterminado: 1.00). |
| `width` | INT | No | 0 a 8192 | El ancho objetivo en píxeles. Obligatorio cuando `resize_type` es `SCALE_DIMENSIONS` o `SCALE_WIDTH` (predeterminado: 512). |
| `height` | INT | No | 0 a 8192 | La altura objetivo en píxeles. Obligatorio cuando `resize_type` es `SCALE_DIMENSIONS` o `SCALE_HEIGHT` (predeterminado: 512). |
| `crop` | COMBO | No | `"disabled"`<br>`"center"` | El método de recorte a aplicar cuando las dimensiones no coinciden con la relación de aspecto. Solo disponible cuando `resize_type` es `SCALE_DIMENSIONS` o `MATCH_SIZE` (predeterminado: "center"). |
| `longer_size` | INT | No | 0 a 8192 | El tamaño objetivo para el lado más largo de la imagen. Obligatorio cuando `resize_type` es `SCALE_LONGER_DIMENSION` (predeterminado: 512). |
| `shorter_size` | INT | No | 0 a 8192 | El tamaño objetivo para el lado más corto de la imagen. Obligatorio cuando `resize_type` es `SCALE_SHORTER_DIMENSION` (predeterminado: 512). |
| `megapixels` | FLOAT | No | 0.01 a 16.0 | El número total objetivo de megapíxeles. Obligatorio cuando `resize_type` es `SCALE_TOTAL_PIXELS` (predeterminado: 1.0). |
| `match` | IMAGE o MASK | No | N/A | Una imagen o máscara cuyas dimensiones se utilizarán para redimensionar la entrada. Obligatorio cuando `resize_type` es `MATCH_SIZE`. |
| `scale_method` | COMBO | Sí | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | El algoritmo de interpolación utilizado para el escalado (predeterminado: "area"). |

**Nota:** El parámetro `crop` solo está disponible y es relevante cuando `resize_type` está configurado como `SCALE_DIMENSIONS` o `MATCH_SIZE`. Al usar `SCALE_WIDTH` o `SCALE_HEIGHT`, la otra dimensión se escala automáticamente para mantener la relación de aspecto original.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `resized` | IMAGE o MASK | La imagen o máscara redimensionada, que coincide con el tipo de dato de la entrada. |

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
