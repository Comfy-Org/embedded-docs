> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/es.md)

Este nodo convierte una imagen rasterizada en un gráfico vectorial escalable (SVG) utilizando los modelos de vectorización de Quiver AI. Envía la imagen a una API externa que la procesa y devuelve el resultado vectorizado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | N/A | Imagen de entrada para vectorizar. |
| `auto_crop` | BOOLEAN | No | `True`<br>`False` | Recortar automáticamente al sujeto dominante. Este es un parámetro avanzado (por defecto: `False`). |
| `model` | DYNAMICCOMBO | Sí | Múltiples opciones disponibles | Modelo a utilizar para la vectorización SVG. Seleccionar un modelo revela parámetros adicionales específicos de ese modelo: `target_size` (tamaño objetivo de redimensionamiento cuadrado en píxeles, por defecto: 1024, rango: 128-4096), `temperature`, `top_p` y `presence_penalty`. |
| `seed` | INT | No | 0 a 2147483647 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente del valor de la semilla. Este parámetro tiene funcionalidad de "control después de generar" (por defecto: 0). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `SVG` | SVG | La salida SVG vectorizada. |