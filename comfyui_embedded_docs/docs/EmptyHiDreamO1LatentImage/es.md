# Imagen Latente Vacía HiDream-O1

Este nodo crea una imagen latente vacía en el espacio de píxeles, diseñado específicamente para el modelo HiDream-O1-Image. Genera un tensor de ceros que sirve como punto de partida para la generación de imágenes, con dimensiones definidas por las entradas `width`, `height` y `batch_size`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente en píxeles (por defecto: 2048). El modelo fue entrenado a ~4 megapíxeles; resoluciones más bajas se salen de la distribución y la calidad disminuye notablemente. | INT | Sí | 64 a 4096 (paso: 32) |
| `alto` | La altura de la imagen latente en píxeles (por defecto: 2048). El modelo fue entrenado a ~4 megapíxeles; resoluciones más bajas se salen de la distribución y la calidad disminuye notablemente. | INT | Sí | 64 a 4096 (paso: 32) |
| `tamaño_lote` | El número de imágenes latentes a generar en un solo lote (por defecto: 1). | INT | No | 1 a 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | Un tensor de ceros que representa la imagen latente vacía, con forma (batch_size, 3, height, width). | LATENT |

## Notas

- El modelo HiDream-O1-Image fue entrenado a aproximadamente 4 megapíxeles. El uso de resoluciones significativamente más bajas puede resultar en una calidad de imagen reducida.
- Las resoluciones de entrenamiento incluyen: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/es.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`
