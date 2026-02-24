> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/es.md)

El nodo Ajustar Brillo modifica el brillo de una imagen de entrada. Funciona multiplicando el valor de cada píxel por un factor especificado, asegurando luego que los valores resultantes se mantengan dentro de un rango válido. Un factor de 1.0 deja la imagen sin cambios, valores por debajo de 1.0 la oscurecen y valores por encima de 1.0 la aclaran.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada a ajustar. |
| `factor` | FLOAT | No | 0.0 - 2.0 | Factor de brillo. 1.0 = sin cambio, <1.0 = más oscuro, >1.0 = más brillante. (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen de salida con el brillo ajustado. |
