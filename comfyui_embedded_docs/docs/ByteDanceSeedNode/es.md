# ByteDance Seed

Genera respuestas de texto utilizando los modelos Seed 2.0 de ByteDance. Proporciona un prompt de texto y, opcionalmente, incluye imágenes o videos para contexto multimodal.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo Seed utilizado para generar la respuesta. | DYNAMIC_COMBO | Sí | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Entrada de texto para el modelo. (predeterminado: "") | STRING | Sí | N/A |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (predeterminado: "") | STRING | No | N/A |

### Entradas del modelo (compartidas por Seed 2.0 Pro, Seed 2.0 Lite y Seed 2.0 Mini)

Los tres modelos Seed exponen los mismos subparámetros cuando se seleccionan.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Controla la aleatoriedad. 0.0 es determinista, los valores más altos son más aleatorios. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 2.0 (paso: 0.01) |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagen(es) opcional(es) para usar como contexto para el modelo. Hasta 20 imágenes. Ranura ampliable: conecte de 1 a 20 elementos, p. ej. `image_1` a `image_20`. | IMAGE | No | 0 a 20 imágenes |
| `videos` | Video(s) opcional(es) para usar como contexto para el modelo. Hasta 4 videos. Ranura ampliable: conecte de 1 a 4 elementos, p. ej. `video_1` a `video_4`. | VIDEO | No | 0 a 4 videos |

**Nota:** El parámetro `model` es un combo dinámico que expone los subparámetros de referencia y temperatura cuando se selecciona un modelo. Puede conectar entradas de imagen y video a este parámetro para proporcionar contexto multimodal. Se admiten un máximo de 20 imágenes y 4 videos por solicitud, y `prompt` es obligatorio y debe contener al menos un carácter que no sea espacio en blanco.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-----------------|-------------|---------------|
| `output` | La respuesta de texto generada por el modelo Seed. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/es.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
