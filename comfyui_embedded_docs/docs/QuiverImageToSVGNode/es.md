Este nodo convierte una imagen rasterizada en un gráfico vectorial escalable (SVG) utilizando los modelos de vectorización de Quiver AI. Envía la imagen a una API externa que la procesa y devuelve el resultado vectorizado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Imagen de entrada para vectorizar. | IMAGE | Sí | N/A |
| `recorte_automático` | Recortar automáticamente al sujeto dominante. Este es un parámetro avanzado (predeterminado: `False`). | BOOLEAN | No | `True`<br>`False` |
| `modelo` | Modelo a utilizar para la vectorización SVG. Al seleccionar un modelo se revelan parámetros adicionales específicos de ese modelo: `target_size` (destino de redimensionamiento cuadrado en píxeles, predeterminado: 1024, rango: 128-4096), `temperature`, `top_p` y `presence_penalty`. | DYNAMICCOMBO | Sí | Múltiples opciones disponibles |
| `semilla` | Semilla para determinar si el nodo debe reejecutarse; los resultados reales son no deterministas independientemente del valor de la semilla. Este parámetro tiene funcionalidad de "control después de generar" (predeterminado: 0). | INT | No | 0 a 2147483647 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `SVG` | La salida SVG vectorizada. | SVG |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/es.md)

---
**Source fingerprint (SHA-256):** `4539277fd6c23aef149c44eeafca4d373cad658d85872de0883245eb4f2479e8`
