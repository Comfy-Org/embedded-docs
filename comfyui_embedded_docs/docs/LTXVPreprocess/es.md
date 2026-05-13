> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/es.md)

El nodo LTXVPreprocess aplica preprocesamiento de compresión a las imágenes. Toma imágenes de entrada y las procesa con un nivel de compresión especificado, generando las imágenes procesadas con la configuración de compresión aplicada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada a procesar |
| `img_compresion` | INT | No | 0-100 | Cantidad de compresión a aplicar en la imagen (predeterminado: 35) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output_image` | IMAGE | La imagen de salida procesada con la compresión aplicada |

---
**Source fingerprint (SHA-256):** `2c5fbde5d011bdf3313ca05508f58a13eaae0bdff12f3659fef281c0045e480d`
