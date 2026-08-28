# ByteDance Seedream 5.0 Pro Separación de Capas

ByteDance Seedream 5.0 Pro Layer Separation descompone una imagen en una placa de fondo más hasta 16 capas transparentes, cada una con su propio orden de apilamiento, cuadro delimitador, nombre y descripción. Devuelve el fondo, imágenes por capa con máscaras, cajas de colocación y una pila de capas lista para editar.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | La imagen a separar. Exactamente una imagen, de al menos 512x512 píxeles, con una relación de aspecto entre 1:16 y 16:1. Las entradas de más de aproximadamente 4 MP se reducen de escala antes de la carga. | IMAGE | Sí | Una sola imagen |
| `prompt` | Cómo separar la imagen. Déjelo vacío para detectar y separar automáticamente todos los elementos principales. Describa los elementos en lenguaje natural para controlar la separación, o apunte a regiones exactas con etiquetas `<bbox>left top right bottom</bbox>` (coordenadas en por mil de 0 a 1000). Valor predeterminado: cadena vacía. | STRING | Sí | Texto multilínea |
| `tamaño` | Nivel de resolución de salida. "auto" sigue el tamaño de la imagen de entrada (limitado al rango de 1K a 2K). Valor predeterminado: "auto". | COMBO | Sí | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `semilla` | Semilla para usar en la generación. Valor predeterminado: 0. | INT | Sí | 0 a 2147483647 |
| `optimización_prompt` | Modo de optimización de prompt: "standard" ofrece mayor calidad, "fast" un tiempo de generación más corto. Valor predeterminado: "standard". | COMBO | No | "standard"<br>"fast" |
| `marca_de_agua` | Si se debe añadir una marca de agua "AI generated" a las imágenes. Valor predeterminado: false. | BOOLEAN | No | false<br>true |
| `recortar_capas` | Geometría de las salidas por lotes de capas/máscaras (layer_stack no se ve afectado y siempre es ajustado). Lienzo completo: cada capa sobre un lienzo de tamaño base en la posición de su cuadro delimitador; recomponer directamente con ImageCompositeMasked. Tamaño mínimo: cada capa recortada a su cuadro delimitador (rellenada hasta la capa más grande para el procesamiento por lotes): tensores mucho más pequeños; reconstruya la colocación con Layers From Bounding Boxes utilizando la salida bboxes. Valor predeterminado: false (lienzo completo). | BOOLEAN | No | false (lienzo completo)<br>true (tamaño mínimo) |

Nota: La entrada `image` debe ser una sola imagen; no se admiten lotes. La imagen debe tener al menos 512x512 píxeles con una relación de aspecto entre 1:16 y 16:1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imagen_base` | La imagen base (placa de fondo) sobre la que se apilan las capas. | IMAGE |
| `máscara_base` | Transparencia de la imagen base (1 = transparente, convención de LoadImage); actualmente siempre totalmente opaca. | MASK |
| `capas` | Capas transparentes ordenadas de abajo hacia arriba. Modo de lienzo completo: colocadas sobre un lienzo negro de tamaño base en la posición de su cuadro delimitador. Modo de tamaño mínimo: recortadas a su cuadro delimitador, ancladas en la esquina superior izquierda, con relleno hasta la capa más grande. | IMAGE |
| `máscaras` | Transparencia por capa, alineada por índice con el lote de capas (1 = transparente, convención de LoadImage). Para composición estilo ImageCompositeMasked, añada InvertMask primero. | MASK |
| `bboxes` | Una caja de colocación por capa, alineada por índice con el lote de capas (introduzca ambas, más las máscaras, en Layers From Bounding Boxes para reconstruir la colocación por capa): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` es la región de contenido de la capa dentro de su propio marco; aterriza en el lienzo en la posición de la caja más ese desplazamiento. | BOUNDING_BOX |
| `pila_de_capas` | Documento de capas listo para editar para Create Layered Image: la placa base más cada elemento como su propia capa nombrada y recortada a su contenido, en su posición real y orden de apilamiento. Conéctelo directamente, o extiéndalo con Add Layer. | LAYERS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/es.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
