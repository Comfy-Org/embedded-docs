> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/es.md)

Este nodo convierte una imagen rasterizada en un gráfico vectorial escalable (SVG) utilizando los modelos de vectorización de Quiver AI. Envía la imagen a una API externa que la procesa y devuelve el resultado vectorizado.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | N/A | Imagen de entrada para vectorizar. |
| `auto_crop` | BOOLEAN | No | `True`<br>`False` | Recortar automáticamente al sujeto dominante. Este es un parámetro avanzado (predeterminado: `False`). |
| `model` | DYNAMICCOMBO | Sí | Múltiples opciones disponibles | Modelo a utilizar para la vectorización SVG. Al seleccionar un modelo se revelan parámetros adicionales específicos de ese modelo: `target_size` (destino de redimensionamiento cuadrado en píxeles, predeterminado: 1024, rango: 128-4096), `temperature`, `top_p` y `presence_penalty`. |
| `seed` | INT | No | 0 a 2147483647 | Semilla para determinar si el nodo debe reejecutarse; los resultados reales son no deterministas independientemente del valor de la semilla. Este parámetro tiene funcionalidad de "control después de generar" (predeterminado: 0). |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `SVG` | SVG | La salida SVG vectorizada. |

---
**Source fingerprint (SHA-256):** `4539277fd6c23aef149c44eeafca4d373cad658d85872de0883245eb4f2479e8`
