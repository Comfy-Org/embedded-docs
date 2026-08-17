# ByteDance Seed

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo Seed utilizado para generar la respuesta. | DYNAMIC_COMBO | Sí | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Entrada de texto para el modelo. (por defecto: "") | STRING | Sí | N/A |
| `seed` | Seed controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. (por defecto: 0) | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (por defecto: "") | STRING | No | N/A |

### Entradas de Seed 2.0 Pro, Seed 2.0 Lite y Seed 2.0 Mini

Esta configuración es compartida por las tres opciones de modelo.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `temperature` | Controla la aleatoriedad. 0.0 es determinista, los valores más altos son más aleatorios. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 2.0 |

### Entradas de referencia

El selector `model` proporciona estos espacios ampliables, que conectan imágenes y videos para darle al modelo contexto multimodal.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Imagen(es) opcional(es) para usar como contexto del modelo. Hasta 20 imágenes. Espacio ampliable: conectar de 1 a 20 elementos (p. ej. `image_1`...`image_20`). | IMAGE | No | `image_1` a `image_20` |
| `videos` | Video(s) opcional(es) para usar como contexto del modelo. Hasta 4 videos. Espacio ampliable: conectar de 1 a 4 elementos (p. ej. `video_1`...`video_4`). | VIDEO | No | `video_1` a `video_4` |

**Nota:** El selector `model` determina qué modelo Seed se utiliza para generar la respuesta. Cada opción se corresponde con un ID de modelo específico: `"Seed 2.0 Pro"` → `seed-2-0-pro-260328`, `"Seed 2.0 Lite"` → `seed-2-0-lite-260228` y `"Seed 2.0 Mini"` → `seed-2-0-mini-260215`.

**Nota sobre restricciones:** Se admite un máximo de 20 imágenes y 4 videos por solicitud. El campo `prompt` debe ser una cadena no vacía.

**Nota sobre precios:** El precio se basa en tokens y se muestra en la interfaz del nodo como un rango aproximado por cada 1K tokens: Seed 2.0 Mini: $0.00025-$0.0009; Seed 2.0 Lite: $0.0003-$0.002; Seed 2.0 Pro: $0.0005-$0.003.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La respuesta de texto generada por el modelo Seed. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/es.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
