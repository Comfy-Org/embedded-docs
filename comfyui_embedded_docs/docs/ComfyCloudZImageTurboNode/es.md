# ComfyCloudZImageTurboNode

Este nodo genera una imagen a partir de un prompt de texto utilizando el modelo Z-Image Turbo, que se completa en solo 8 pasos. La generación se ejecuta de forma remota en las GPU de Comfy Cloud y se factura por tiempo de GPU, lo que la convierte en una de las opciones más rápidas y económicas para iterar sobre ideas de imágenes. Una vez finalizada la generación, el nodo descarga la imagen resultante para usarla en su flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto que describe la imagen a generar. Acepta entrada de varias líneas y se recorta antes del envío. No debe estar vacío después del recorte. | STRING | Sí | 1 - 4096 caracteres |
| `seed` | Semilla aleatoria utilizada para controlar la reproducibilidad de la generación. Cambiarla produce una variación diferente. Incluye una opción de control posterior a la generación. Valor predeterminado: 42. | INT | No | 0 - 18446744073709551615 |
| `aspect_ratio` | Relación de aspecto de la imagen generada. Valor predeterminado: "1:1". | COMBO | No | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Presupuesto total de píxeles. 1.0 equivale aproximadamente a 1024x1024 en una relación cuadrada. Valor predeterminado: 1.0. | FLOAT | No | 0.1 - 16.0<br>(paso de 0.1) |

Nota: Los valores de entrada se validan antes de enviar la generación. El `prompt` debe contener entre 1 y 4096 caracteres después de recortar los espacios en blanco, `aspect_ratio` debe ser una de las opciones enumeradas, y `megapixels` debe ingresarse en incrementos de 0.1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `IMAGE` | La imagen generada se devuelve como un tensor de imagen listo para su posterior procesamiento o para nodos de guardado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/es.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`
