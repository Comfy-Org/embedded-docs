# ByteDance Seedream 5.0 Pro Separación de Capas

ByteDance Seedream 5.0 Pro Layer Separation descompone una imagen en una placa de fondo más hasta 16 capas transparentes, cada una con su propio orden de apilamiento, cuadro delimitador, nombre y descripción. Devuelve el fondo, las imágenes por capa con máscaras, las cajas de colocación y una pila de capas lista para editar.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | La imagen a separar. Exactamente una imagen, de al menos 512x512 píxeles, con una relación de aspecto entre 1:16 y 16:1. Las imágenes de entrada de más de aproximadamente 4 MP se reducen de escala antes de subirse. | IMAGE | Sí | Imagen única |
| `prompt` | Cómo separar la imagen. Déjalo vacío para autodetectar y separar todos los elementos principales. Describe elementos en lenguaje natural para controlar la separación, o apunta a regiones exactas con etiquetas `<bbox>left top right bottom</bbox>` (coordenadas por mil entre 0 y 1000). Predeterminado: cadena vacía. | STRING | Sí | Texto multilínea |
| `size` | Nivel de resolución de salida. "auto" sigue el tamaño de la imagen de entrada (limitado al rango de 1K a 2K). Predeterminado: "auto". | COMBO | Sí | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Semilla para la generación. Predeterminado: 0. | INT | Sí | 0 a 2147483647 |
| `prompt_optimization` | Modo de optimización del prompt: "standard" ofrece mayor calidad, "fast" un tiempo de generación más corto. Predeterminado: "standard". | COMBO | No | "standard"<br>"fast" |
| `watermark` | Si se debe añadir una marca de agua "AI generated" a las imágenes. Predeterminado: false. | BOOLEAN | No | false<br>true |
| `crop_layers` | Geometría de las salidas en lote de capas/máscaras (layer_stack no se ve afectado y siempre está ajustado). Lienzo completo: cada capa sobre un lienzo del tamaño base en la posición de su cuadro delimitador: recomponer directamente con ImageCompositeMasked. Tamaño mínimo: cada capa recortada a su cuadro delimitador (rellenada hasta la capa más grande para el procesamiento por lotes): tensores mucho más pequeños; reconstruir la colocación con Layers From Bounding Boxes usando la salida bboxes. Predeterminado: false (lienzo completo). | BOOLEAN | No | false (lienzo completo)<br>true (tamaño mínimo) |

Nota: La imagen de entrada debe ser una sola imagen; no se admiten lotes. La imagen debe tener al menos 512x512 píxeles con una relación de aspecto entre 1:16 y 16:1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `base_image` | La imagen base (placa de fondo) sobre la que se apilan las capas. | IMAGE |
| `base_mask` | Transparencia de la imagen base (1 = transparente, convención de LoadImage); actualmente siempre totalmente opaca. | MASK |
| `layers` | Capas transparentes ordenadas de abajo hacia arriba. Modo de lienzo completo: colocadas sobre un lienzo negro del tamaño base en la posición de su cuadro delimitador. Modo de tamaño mínimo: recortadas a su cuadro delimitador, ancladas en la esquina superior izquierda y rellenadas hasta la capa más grande. | IMAGE |
| `masks` | Transparencia por capa, alineada por índice con el lote de capas (1 = transparente, convención de LoadImage). Para composición estilo ImageCompositeMasked, añade InvertMask primero. | MASK |
| `bboxes` | Una caja de colocación por capa, alineada por índice con el lote de capas (introduce ambos, junto con las máscaras, en Layers From Bounding Boxes para reconstruir la colocación de cada capa): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` es la región de contenido de la capa dentro de su propio marco; se sitúa sobre el lienzo en la posición de la caja más ese desplazamiento. | BOUNDING_BOX |
| `layer_stack` | Documento de capas listo para editar para Create Layered Image: la placa de fondo más cada elemento como su propia capa con nombre, recortada con ajuste, en su posición y orden de apilamiento reales. Conéctalo directamente o amplíalo con Add Layer. | LAYERS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/es.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
