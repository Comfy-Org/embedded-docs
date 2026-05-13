> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/es.md)

El nodo Reve Image Remix utiliza la API de Reve para generar una nueva imagen. Combina una o más imágenes de referencia con un mensaje de texto para crear una nueva imagen remezclada basada en la descripción proporcionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imágenes_de_referencia` | IMAGE | Sí | 1 a 6 imágenes | Una o más imágenes de referencia para usar como base para la remezcla. Puedes agregar entre 1 y 6 imágenes. |
| `prompt` | STRING | Sí | 1 a 2560 caracteres | Una descripción textual de la imagen deseada. Puedes incluir etiquetas XML `<img>` para hacer referencia a imágenes específicas por su índice (por ejemplo, `<img>0</img>`, `<img>1</img>`). (predeterminado: vacío) |
| `modelo` | COMBO | Sí | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | La versión del modelo a utilizar para la remezcla. Cada opción de modelo incluye relaciones de aspecto configurables y escalado durante la prueba. |
| `escalar` | COMBO | No | `"disabled"`<br>`"enabled"` | Controla si se debe aumentar la resolución de la imagen generada. Cuando está habilitado, puedes seleccionar un factor de ampliación. |
| `eliminar_fondo` | BOOLEAN | No | `true`<br>`false` | Cuando está habilitado, intenta eliminar el fondo de la imagen generada. |
| `semilla` | INT | No | 0 a 2147483647 | Un valor de semilla. Cambiar este valor hará que el nodo se ejecute nuevamente, pero los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) |

**Nota:** El parámetro `model` es un combo dinámico que incluye configuraciones anidadas para `aspect_ratio` (opciones: "auto", "16:9", "9:16", "3:2", "2:3", "4:3", "3:4", "1:1") y `test_time_scaling`. El parámetro `upscale`, cuando se establece en "enabled", revela una configuración anidada de `upscale_factor`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La nueva imagen generada por el proceso de remezcla de Reve. |

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
