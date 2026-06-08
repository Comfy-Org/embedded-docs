# Descripción general

Este nodo crea una imagen latente vacía en el espacio de píxeles, diseñada específicamente para el modelo HiDream-O1-Image. Genera un tensor en blanco de ceros que sirve como punto de partida para la generación de imágenes, con dimensiones definidas por las entradas de ancho, alto y tamaño de lote.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente en píxeles (predeterminado: 2048). El modelo fue entrenado a ~4 megapíxeles; resoluciones más bajas se desvían de la distribución y la calidad disminuye notablemente. | INT | Sí | 64 a 4096 (paso: 32) |
| `alto` | El alto de la imagen latente en píxeles (predeterminado: 2048). El modelo fue entrenado a ~4 megapíxeles; resoluciones más bajas se desvían de la distribución y la calidad disminuye notablemente. | INT | Sí | 64 a 4096 (paso: 32) |
| `tamaño_lote` | La cantidad de imágenes latentes a generar en un solo lote (predeterminado: 1). | INT | No | 1 a 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | Un tensor lleno de ceros que representa la imagen latente vacía, con forma (batch_size, 3, height, width). | LATENT |

## Notas

- El modelo HiDream-O1-Image fue entrenado aproximadamente a 4 megapíxeles. El uso de resoluciones significativamente más bajas puede resultar en una calidad de imagen reducida.
- Las resoluciones de entrenamiento incluyen: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/es.md)

---
**Source fingerprint (SHA-256):** `fca32bbeddf120b4a7f9a9b88814f5345db133b35252c4d86079397be350c15e`
