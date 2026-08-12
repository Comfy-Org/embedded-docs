# ByteDanceSeedreamLayerSeparationNode

ByteDance Seedream 5.0 Pro Layer Separation descompone una imagen en una capa de fondo y hasta 16 capas transparentes, cada una con su propio orden de apilamiento, cuadro delimitador, nombre y descripción. Devuelve el fondo, las imágenes por capa con sus máscaras, los cuadros de colocación y una pila de capas lista para editar.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `image` | La imagen a separar. Exactamente una sola imagen, de al menos 512x512 píxeles, con una relación de aspecto entre 1:16 y 16:1. Las imágenes de entrada de más de aproximadamente 4 MP se reducen de escala antes de subirse. | IMAGE | Sí | Imagen única |
| `prompt` | Cómo separar la imagen. Déjelo vacío para detectar automáticamente y separar todos los elementos principales. Describa los elementos en lenguaje natural para controlar la separación, o apunte a regiones exactas con las etiquetas `<bbox>left top right bottom</bbox>` (coordenadas por mil de 0 a 1000). Predeterminado: cadena vacía. | STRING | Sí | Texto multilínea |
| `size` | Nivel de resolución de salida. «auto» sigue el tamaño de la imagen de entrada (limitado al rango de 1K a 2K). Predeterminado: «auto». | STRING | Sí | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Semilla que se utilizará para la generación. Predeterminado: 0. | INT | Sí | 0 a 2147483647 |
| `prompt_optimization` | Modo de optimización del prompt: «standard» ofrece mayor calidad, «fast» un tiempo de generación más corto. Predeterminado: «standard». | STRING | No | "standard"<br>"fast" |
| `watermark` | Indica si se debe añadir una marca de agua «generado por IA» a las imágenes. Predeterminado: false. | BOOLEAN | No | false<br>true |
| `crop_layers` | Geometría de las salidas por lotes de capas/máscaras (layer_stack no se ve afectada y siempre está ajustada). Lienzo completo: cada capa se coloca en un lienzo del tamaño de la base en la posición de su cuadro delimitador; recomponga directamente con ImageCompositeMasked. Tamaño mínimo: cada capa se recorta a su cuadro delimitador (con relleno hasta la capa más grande para el procesamiento por lotes), lo que genera tensores mucho más pequeños; reconstruya la colocación con Layers From Bounding Boxes usando la salida bboxes. Predeterminado: false (lienzo completo). | BOOLEAN | No | false (lienzo completo)<br>true (tamaño mínimo) |

Nota: La imagen de entrada debe ser una sola imagen; no se admiten lotes. La imagen debe tener al menos 512x512 píxeles con una relación de aspecto entre 1:16 y 16:1.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `base_image` | La imagen base (placa de fondo) sobre la que se apilan las capas. | IMAGE |
| `base_mask` | Transparencia de la imagen base (1 = transparente, convención de LoadImage); actualmente siempre totalmente opaca. | MASK |
| `layers` | Capas transparentes ordenadas de abajo hacia arriba. Modo de lienzo completo: colocadas en un lienzo negro del tamaño de la base en la posición de su cuadro delimitador. Modo de tamaño mínimo: recortadas a su cuadro delimitador, ancladas en la esquina superior izquierda y rellenadas hasta la capa más grande. | IMAGE |
| `masks` | Transparencia por capa, alineada por índice con el lote de capas (1 = transparente, convención de LoadImage). Para la composición estilo ImageCompositeMasked, agregue InvertMask primero. | MASK |
| `bboxes` | Un cuadro de ubicación por capa, alineado por índice con el lote de capas (introduzca ambos, junto con las máscaras, en Layers From Bounding Boxes para reconstruir la ubicación de cada capa): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` es la región de contenido de la capa dentro de su propio marco; se coloca en el lienzo en la posición del cuadro más ese desplazamiento. | BOUNDING_BOX |
| `layer_stack` | Documento de capas listo para editar para Create Layered Image: la placa de fondo más cada elemento como su propia capa con nombre y recorte ajustado, en su posición real y orden de apilamiento. Conéctelo directamente o amplíelo con Add Layer. | LAYERS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/es.md)

---
**Source fingerprint (SHA-256):** `059d0a1a5f5793aadda72f50b549b8b10e2ecae3ce003f82c0c28191c3460954`
