> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/es.md)

Escalar imagen con alteraciones mínimas a resolución 4K. Este nodo utiliza el escalado conservador de Stability AI para aumentar la resolución de la imagen mientras preserva el contenido original y realiza solo cambios sutiles.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a escalar |
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen de salida. Un prompt fuerte y descriptivo que defina claramente elementos, colores y sujetos producirá mejores resultados. (valor por defecto: cadena vacía) |
| `creatividad` | FLOAT | Sí | 0.2-0.5 | Controla la probabilidad de crear detalles adicionales no fuertemente condicionados por la imagen inicial. (valor por defecto: 0.35) |
| `semilla` | INT | Sí | 0-4294967294 | La semilla aleatoria utilizada para crear el ruido. (valor por defecto: 0) |
| `prompt negativo` | STRING | No | - | Palabras clave de lo que no deseas ver en la imagen de salida. Esta es una característica avanzada. (valor por defecto: cadena vacía) |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La imagen escalada a resolución 4K |
