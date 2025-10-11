> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/es.md)

El nodo HunyuanRefinerLatent procesa acondicionamientos y entradas latentes para operaciones de refinamiento. Aplica aumento de ruido tanto al acondicionamiento positivo como al negativo mientras incorpora datos de imagen latente, y genera una nueva salida latente con dimensiones específicas para su posterior procesamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de acondicionamiento positivo a procesar |
| `negative` | CONDITIONING | Sí | - | La entrada de acondicionamiento negativo a procesar |
| `latent` | LATENT | Sí | - | La entrada de representación latente |
| `noise_augmentation` | FLOAT | Sí | 0.0 - 1.0 | La cantidad de aumento de ruido a aplicar (por defecto: 0.10) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El acondicionamiento positivo procesado con aumento de ruido aplicado y concatenación de imagen latente |
| `negative` | CONDITIONING | El acondicionamiento negativo procesado con aumento de ruido aplicado y concatenación de imagen latente |
| `latent` | LATENT | Una nueva salida latente con dimensiones [batch_size, 32, height, width, channels] |