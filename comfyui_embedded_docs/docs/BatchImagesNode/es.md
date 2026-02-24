> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/es.md)

El nodo Batch Images combina múltiples imágenes individuales en un lote único. Toma un número variable de entradas de imagen y las emite como un único tensor de imágenes en lote, permitiendo que sean procesadas juntas en nodos posteriores.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | 2 a 50 entradas | Una lista dinámica de entradas de imagen. Puedes añadir entre 2 y 50 imágenes para combinarlas en un lote. La interfaz del nodo te permite añadir más ranuras de entrada de imagen según sea necesario. |

**Nota:** Debes conectar al menos dos imágenes para que el nodo funcione. La primera ranura de entrada siempre es obligatoria, y puedes añadir más usando el botón "+" que aparece en la interfaz del nodo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | Un único tensor de imágenes en lote que contiene todas las imágenes de entrada apiladas juntas. |
