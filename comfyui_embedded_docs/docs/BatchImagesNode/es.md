> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/es.md)

El nodo "Combinar Imágenes" agrupa múltiples imágenes individuales en un solo lote. Toma una cantidad variable de entradas de imagen y las envía como un único tensor de imágenes agrupadas, lo que permite procesarlas juntas en nodos posteriores.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imágenes` | IMAGE | Sí | 2 a 50 entradas | Una lista dinámica de entradas de imagen. Puedes agregar entre 2 y 50 imágenes para combinarlas en un lote. La interfaz del nodo te permite añadir más ranuras de entrada de imagen según sea necesario. |

**Nota:** Debes conectar al menos dos imágenes para que el nodo funcione. La primera ranura de entrada siempre es obligatoria, y puedes agregar más usando el botón "+" que aparece en la interfaz del nodo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | Un único tensor de imágenes agrupadas que contiene todas las imágenes de entrada apiladas juntas. |

---
**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`
