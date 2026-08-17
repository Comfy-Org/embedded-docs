# Reve Crear Imagen

El nodo Reve Image Create genera imágenes a partir de descripciones de texto utilizando el modelo Reve AI. Envía un prompt de texto a la API de Reve y devuelve la imagen generada. Puedes controlar la relación de aspecto de la imagen y aplicar efectos opcionales de posprocesamiento como ampliación y eliminación de fondo. Este nodo está obsoleto.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | Versión del modelo a utilizar para la generación. Al seleccionar este modelo se muestran los ajustes `aspect_ratio` y `test_time_scaling`. | DYNAMIC_COMBO | Sí | `"reve-create@20250915"` |
| `prompt` | Descripción en texto de la imagen deseada. Máximo 2560 caracteres. Predeterminado: vacío. | STRING | Sí | N/A |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Predeterminado: 0. | INT | No | 0 a 2147483647 |
| `upscale` | Amplía la imagen generada. Puede añadir un costo adicional. Cuando se establece en `enabled`, aparece el ajuste `upscale_factor`. Predeterminado: `disabled`. | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Elimina el fondo de la imagen generada. Puede añadir un costo adicional. Predeterminado: false. | BOOLEAN | No | true<br>false |

### Entradas de reve-create@20250915

Estos ajustes aparecen cuando `model` está establecido en `"reve-create@20250915"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Relación de aspecto de la imagen de salida. | COMBO | Sí | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Los valores más altos producen mejores imágenes pero cuestan más créditos. Predeterminado: 1. | INT | No | 1 a 5 |

### Entradas de ampliación

Estos ajustes aparecen cuando `upscale` está establecido en `"enabled"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Factor de ampliación (2x, 3x o 4x). Predeterminado: 2. | INT | No | 2 a 4 (paso 1) |

**Nota:** El parámetro `seed` no garantiza salidas deterministas. El parámetro `upscale` controla si la ampliación se aplica como paso de posprocesamiento.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La imagen generada por el modelo Reve a partir del prompt de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/es.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
