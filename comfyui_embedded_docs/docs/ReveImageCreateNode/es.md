El nodo Crear Imagen Reve genera imágenes a partir de descripciones textuales utilizando el modelo Reve AI. Envía un mensaje de texto a la API de Reve y devuelve la imagen generada. Puedes controlar la relación de aspecto de la imagen y aplicar efectos opcionales de posprocesamiento, como el escalado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Descripción textual de la imagen deseada. Máximo 2560 caracteres. | STRING | Sí | N/A |
| `modelo` | Versión del modelo y relación de aspecto a utilizar para la generación. La primera opción selecciona el modelo, y las opciones siguientes definen la relación de aspecto de la imagen. | COMBO | Sí | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `escalar` | Activa o desactiva el paso de posprocesamiento de escalado. Cuando está activado, también debes seleccionar un factor de escalado. | COMBO | No | `"disabled"`<br>`"enabled"` |
| `upscale_factor` | El factor por el cual se incrementa la resolución de la imagen. Este parámetro solo está activo cuando `escalar` está configurado como `"enabled"`. | COMBO | No | `2`<br>`3`<br>`4` |
| `eliminar_fondo` | Cuando está activado, aplica un paso de posprocesamiento de eliminación de fondo a la imagen generada. | BOOLEAN | No | N/A |
| `semilla` | Un valor de semilla que controla si el nodo debe reejecutarse. Nota: Los resultados no son deterministas independientemente del valor de la semilla. Valor predeterminado: 0. | INT | No | 0 a 2147483647 |

**Nota:** El parámetro `upscale_factor` depende de que el parámetro `upscale` esté configurado como `"enabled"`. El parámetro `seed` no garantiza resultados deterministas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen generada por el modelo Reve basada en el mensaje de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/es.md)

---
**Source fingerprint (SHA-256):** `56cb32ad254d39609d9795ca29f1ccba1db2c5a7ac5bb530475298306ec4ea19`
