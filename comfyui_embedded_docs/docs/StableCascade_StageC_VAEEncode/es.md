> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/es.md)

El nodo StableCascade_StageC_VAEEncode procesa imágenes a través de un codificador VAE para generar representaciones latentes para modelos Stable Cascade. Toma una imagen de entrada y la comprime utilizando el modelo VAE especificado, luego genera dos representaciones latentes: una para la etapa C y un marcador de posición para la etapa B. El parámetro de compresión controla cuánto se reduce la escala de la imagen antes de la codificación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que será codificada en el espacio latente |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen |
| `compresión` | INT | No | 4-128 | El factor de compresión aplicado a la imagen antes de la codificación (por defecto: 42) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `etapa_b` | LATENT | La representación latente codificada para la etapa C del modelo Stable Cascade |
| `stage_b` | LATENT | Una representación latente de marcador de posición para la etapa B (actualmente devuelve ceros) |
