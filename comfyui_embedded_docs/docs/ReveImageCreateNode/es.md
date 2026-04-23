> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/es.md)

El nodo Reve Image Create genera imágenes a partir de descripciones de texto utilizando el modelo Reve AI. Envía un mensaje de texto a la API de Reve y devuelve la imagen generada. Puedes controlar la relación de aspecto de la imagen y aplicar efectos opcionales de posprocesamiento como el aumento de resolución.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción de texto de la imagen deseada. Máximo 2560 caracteres. |
| `model` | COMBO | Sí | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Versión del modelo y relación de aspecto a utilizar para la generación. La primera opción selecciona el modelo, y las opciones posteriores definen la relación de aspecto de la imagen. |
| `upscale` | COMBO | No | `"disabled"`<br>`"enabled"` | Habilita o deshabilita el paso de posprocesamiento de aumento de resolución. Cuando está habilitado, también debes seleccionar un factor de aumento. |
| `upscale_factor` | COMBO | No | `2`<br>`3`<br>`4` | El factor por el cual se aumenta la resolución de la imagen. Este parámetro solo está activo cuando `upscale` está configurado en `"enabled"`. |
| `remove_background` | BOOLEAN | No | N/A | Cuando está habilitado, aplica un paso de posprocesamiento de eliminación de fondo a la imagen generada. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla que controla si el nodo debe volver a ejecutarse. Nota: Los resultados no son deterministas independientemente del valor de la semilla. Por defecto: 0. |

**Nota:** El parámetro `upscale_factor` depende de que el parámetro `upscale` esté configurado en `"enabled"`. El parámetro `seed` no garantiza salidas deterministas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen generada por el modelo Reve basada en el mensaje de entrada. |