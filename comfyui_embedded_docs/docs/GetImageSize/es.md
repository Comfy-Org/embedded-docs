El nodo GetImageSize extrae las dimensiones e información de lote de una imagen de entrada. Devuelve el ancho, alto y tamaño de lote de la imagen, mostrando también esta información como texto de progreso en la interfaz del nodo. Los datos de la imagen original pasan sin modificaciones.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada de la cual extraer información de tamaño | IMAGE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `alto` | El ancho de la imagen de entrada en píxeles | INT |
| `tamaño_de_lote` | El alto de la imagen de entrada en píxeles | INT |
| `batch_size` | El número de imágenes en el lote | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/es.md)

---
**Source fingerprint (SHA-256):** `5cd19ae762d2403c6c5d0740cd5f8c17913daea737fddcff8f0d9da2210e82ab`
