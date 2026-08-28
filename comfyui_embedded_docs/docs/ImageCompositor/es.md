# ImageCompositor

Este nodo combina múltiples capas de imagen en una única imagen compuesta. Toma una pila de capas construida con el nodo Add Layer y, opcionalmente, una composición guardada desde el editor de compositor; luego fusiona las capas utilizando su posición, tamaño, rotación, opacidad y configuración de modo de mezcla.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `capas` | Pila de capas para componer; constrúyala con Add Layer. Los elementos se apilan por z_index, los fotogramas de lote dentro de un elemento se expanden a capas consecutivas, y la posición, opacidad y modo de mezcla del elemento definen la composición inicial. Sin un lienzo de documento explícito, el tamaño es el alcance máximo de las capas colocadas según el mejor esfuerzo. Una composición guardada que coincida con las entradas actuales tiene prioridad. | LAYERS | Sí | Máximo 50 capas |
| `compositor` | Composición en capas guardada por el editor de compositor. | COMPOSITOR | No | Ninguno |

**Notas sobre las restricciones:**

- La pila de capas admite un máximo de 50 capas (fotogramas expandidos); proporcionar más genera un error.
- Solo se admiten capas rasterizadas actualmente; otros tipos de elementos de capa generan un error.
- La versión del documento `layers` debe ser 1; otras versiones generan un error.
- El estado guardado de `compositor` solo se reproduce cuando sus huellas de entrada registradas coinciden con la pila de capas actual. Si no coinciden, el nodo recurre a componer desde las propiedades de las capas y marca el estado guardado como obsoleto.
- La opacidad de la capa se limita al rango de 0.0 a 1.0.
- La colocación horizontal/vertical de la capa (`x`, `y`) se limita al límite máximo de resolución.
- El ancho y la altura de la capa vuelven al tamaño natural de la imagen cuando se configuran en cero o menos, y están limitados al máximo de resolución.
- El tamaño del lienzo compuesto no debe exceder el límite máximo de resolución.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| IMAGE | Imagen compuesta. Lleva un canal alfa cuando la composición tiene áreas transparentes (por ejemplo, fondo oculto); de lo contrario, RGB simple. | IMAGE |
| MASK | Transparencia de la composición (1 = completamente transparente). Todos ceros cuando la composición es opaca. | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/es.md)

---
**Source fingerprint (SHA-256):** `1eca5c151b3737ccf76e6fd7a83cd1458b2acc314609753d597eec711bcf4bd8`
