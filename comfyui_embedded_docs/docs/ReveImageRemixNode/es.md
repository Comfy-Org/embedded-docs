# Reve Mezclar Imagen

El nodo Reve Image Remix utiliza la API de Reve para generar una nueva imagen. Combina una o más imágenes de referencia con un mensaje de texto para crear una nueva imagen remezclada basada en la descripción proporcionada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes_de_referencia` | Una o más imágenes de referencia para usar como base para la remezcla. Puedes agregar entre 1 y 6 imágenes. | IMAGE | Sí | 1 a 6 imágenes |
| `prompt` | Una descripción textual de la imagen deseada. Puedes incluir etiquetas XML `<img>` para hacer referencia a imágenes específicas por su índice (por ejemplo, `<img>0</img>`, `<img>1</img>`). (predeterminado: vacío) | STRING | Sí | 1 a 2560 caracteres |
| `modelo` | La versión del modelo a utilizar para la remezcla. Cada opción de modelo incluye relaciones de aspecto configurables y escalado durante la prueba. | COMBO | Sí | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `escalar` | Controla si se debe aumentar la resolución de la imagen generada. Cuando está habilitado, puedes seleccionar un factor de ampliación. | COMBO | No | `"disabled"`<br>`"enabled"` |
| `eliminar_fondo` | Cuando está habilitado, intenta eliminar el fondo de la imagen generada. | BOOLEAN | No | `true`<br>`false` |
| `semilla` | Un valor de semilla. Cambiar este valor hará que el nodo se ejecute nuevamente, pero los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | No | 0 a 2147483647 |

**Nota:** El parámetro `model` es un combo dinámico que incluye configuraciones anidadas para `aspect_ratio` (opciones: "auto", "16:9", "9:16", "3:2", "2:3", "4:3", "3:4", "1:1") y `test_time_scaling`. El parámetro `upscale`, cuando se establece en "enabled", revela una configuración anidada de `upscale_factor`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La nueva imagen generada por el proceso de remezcla de Reve. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/es.md)

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
