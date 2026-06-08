El nodo Reve Image Edit te permite modificar una imagen existente basándose en una descripción textual. Utiliza la API de Reve para interpretar tus instrucciones y aplicar los cambios solicitados a la imagen que proporcionas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen a editar. | IMAGE | Sí | - |
| `instrucción_de_edición` | Descripción textual de cómo editar la imagen. Máximo 2560 caracteres. | STRING | Sí | - |
| `modelo` | Versión del modelo a utilizar para la edición. | MODEL | Sí | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `model.aspect_ratio` | La relación de aspecto para la imagen editada. Cuando se establece en "auto", la relación de aspecto se determina automáticamente. | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Factor de escalado en tiempo de prueba para el modelo. Valores más altos pueden mejorar la calidad pero aumentan el tiempo de procesamiento. | FLOAT | No | - |
| `escalar` | Controla si se debe escalar la imagen generada. | COMBO | No | `"disabled"`<br>`"enabled"` |
| `upscale.upscale_factor` | El factor por el cual escalar la imagen cuando el escalado está habilitado. | FLOAT | No | - |
| `eliminar_fondo` | Controla si se debe eliminar el fondo de la imagen generada. | BOOLEAN | No | - |
| `semilla` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | No | 0 a 2147483647 |

**Nota:** El parámetro `upscale.upscale_factor` solo es relevante cuando el parámetro `upscale` está configurado como `"enabled"`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La imagen editada generada según la instrucción. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/es.md)

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`
