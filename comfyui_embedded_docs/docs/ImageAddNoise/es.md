> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/es.md)

El nodo ImageAddNoise agrega ruido aleatorio a una imagen de entrada. Utiliza una semilla aleatoria específica para generar patrones de ruido consistentes y permite controlar la intensidad del efecto de ruido. La imagen resultante mantiene las mismas dimensiones que la entrada pero con textura visual añadida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada a la que se le agregará ruido |
| `seed` | INT | Sí | 0 a 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido (valor por defecto: 0) |
| `strength` | FLOAT | Sí | 0.0 a 1.0 | Controla la intensidad del efecto de ruido (valor por defecto: 0.5) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen de salida con el ruido aplicado |