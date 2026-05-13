> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/es.md)

El nodo Reve Image Edit te permite modificar una imagen existente basándose en una descripción textual. Utiliza la API de Reve para interpretar tus instrucciones y aplicar los cambios solicitados a la imagen que proporcionas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen a editar. |
| `edit_instruction` | STRING | Sí | - | Descripción textual de cómo editar la imagen. Máximo 2560 caracteres. |
| `model` | MODEL | Sí | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` | Versión del modelo a utilizar para la edición. |
| `model.aspect_ratio` | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | La relación de aspecto para la imagen editada. Cuando se establece en "auto", la relación de aspecto se determina automáticamente. |
| `model.test_time_scaling` | FLOAT | No | - | Factor de escalado en tiempo de prueba para el modelo. Valores más altos pueden mejorar la calidad pero aumentan el tiempo de procesamiento. |
| `upscale` | COMBO | No | `"disabled"`<br>`"enabled"` | Controla si se debe escalar la imagen generada. |
| `upscale.upscale_factor` | FLOAT | No | - | El factor por el cual escalar la imagen cuando el escalado está habilitado. |
| `remove_background` | BOOLEAN | No | - | Controla si se debe eliminar el fondo de la imagen generada. |
| `seed` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) |

**Nota:** El parámetro `upscale.upscale_factor` solo es relevante cuando el parámetro `upscale` está configurado como `"enabled"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen editada generada según la instrucción. |

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`
