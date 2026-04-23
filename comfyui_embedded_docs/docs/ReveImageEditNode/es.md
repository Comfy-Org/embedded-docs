> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/es.md)

El nodo Reve Image Edit permite modificar una imagen existente basándose en una descripción de texto. Utiliza la API de Reve para interpretar tus instrucciones y aplicar los cambios solicitados a la imagen que proporciones.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen a editar. |
| `edit_instruction` | STRING | Sí | - | Descripción textual de cómo editar la imagen. Máximo 2560 caracteres. |
| `model` | MODEL | Sí | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"`<br>`"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Versión del modelo a utilizar para la edición. Las opciones incluyen versiones específicas del modelo y configuraciones de relación de aspecto. |
| `upscale` | COMBO | No | `"disabled"`<br>`"enabled"` | Controla si se debe aumentar la resolución (upscale) de la imagen generada. |
| `upscale_factor` | FLOAT | No | - | El factor por el cual aumentar la resolución de la imagen cuando el upscaling está habilitado. |
| `remove_background` | BOOLEAN | No | - | Controla si se debe eliminar el fondo de la imagen generada. |
| `seed` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (valor por defecto: 0) |

**Nota:** El parámetro `upscale_factor` solo es relevante cuando el parámetro `upscale` está configurado como `"enabled"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen editada generada basándose en la instrucción. |