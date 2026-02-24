> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/es.md)

El nodo Batch Latents combina múltiples entradas latentes en un solo lote. Toma un número variable de muestras latentes y las fusiona a lo largo de la dimensión del lote, permitiendo que sean procesadas juntas en nodos posteriores. Esto es útil para generar o procesar múltiples imágenes en una sola operación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Sí | N/A | La primera muestra latente que se incluirá en el lote. |
| `latent_2` a `latent_50` | LATENT | No | N/A | Muestras latentes adicionales para incluir en el lote. Puedes añadir entre 2 y 50 entradas latentes en total. |

**Nota:** Debes proporcionar al menos dos entradas latentes para que el nodo funcione. El nodo creará automáticamente ranuras de entrada a medida que conectes más latentes, hasta un máximo de 50.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | Una única salida latente que contiene todas las entradas latentes combinadas en un solo lote. |
