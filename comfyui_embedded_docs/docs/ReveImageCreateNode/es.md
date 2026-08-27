# Reve Crear Imagen

El nodo Reve Image Create genera imágenes a partir de descripciones de texto utilizando el modelo Reve AI. Envía un prompt de texto a la API de Reve y devuelve la imagen generada, con controles para la relación de aspecto y posprocesamiento opcional, como la ampliación y la eliminación del fondo. Este nodo está obsoleto.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Versión del modelo a utilizar para la generación. | DYNAMIC_COMBO | Sí | `"reve-create@20250915"` |
| `prompt` | Descripción de texto de la imagen deseada. Máximo 2560 caracteres. | STRING | Sí | 1 a 2560 caracteres |
| `escalar` | Amplía la imagen generada. Puede añadir un costo adicional. Valor predeterminado: "disabled". | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `eliminar_fondo` | Elimina el fondo de la imagen generada. Puede añadir un costo adicional. Valor predeterminado: False. | BOOLEAN | No | N/A |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Valor predeterminado: 0. | INT | No | 0 a 2147483647 |

### Entradas de reve-create@20250915

Opciones disponibles cuando `model` está configurado en `"reve-create@20250915"`:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Relación de aspecto de la imagen de salida. | COMBO | Sí | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Los valores más altos producen mejores imágenes pero cuestan más créditos. Valor predeterminado: 1. Opción avanzada. | INT | No | 1 a 5 |

### Entradas de Upscale

Opciones disponibles cuando `upscale` está configurado en `"enabled"`:

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Factor de ampliación (2x, 3x o 4x). Valor predeterminado: 2. | INT | No | 2 a 4 |

**Nota:** El parámetro `seed` no garantiza salidas deterministas. El parámetro `upscale` controla si se aplica la ampliación como paso de posprocesamiento y puede añadir un costo adicional. El `prompt` debe contener entre 1 y 2560 caracteres.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `image` | La imagen generada por el modelo Reve a partir del prompt de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/es.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
