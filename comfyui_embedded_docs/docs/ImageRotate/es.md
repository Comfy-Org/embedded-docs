> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/es.md)

El nodo ImageRotate gira una imagen de entrada según ángulos especificados. Soporta cuatro opciones de rotación: sin rotación, 90 grados en sentido horario, 180 grados y 270 grados en sentido horario. La rotación se realiza utilizando operaciones de tensor eficientes que mantienen la integridad de los datos de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a rotar |
| `rotation` | STRING | Sí | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | El ángulo de rotación a aplicar a la imagen |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen de salida rotada |
