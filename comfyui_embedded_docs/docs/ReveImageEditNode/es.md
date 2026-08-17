# Reve Editar Imagen

El nodo Reve Image Edit permite modificar una imagen existente a partir de una descripción textual. Utiliza la API de Reve para interpretar tus instrucciones y aplicar los cambios solicitados a la imagen que proporciones.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La imagen a editar. | IMAGE | Sí | - |
| `edit_instruction` | Descripción textual de cómo editar la imagen. Máximo 2560 caracteres. (por defecto: "") | STRING | Sí | 1 a 2560 caracteres |
| `model` | Versión del modelo a utilizar para la edición. | DYNAMIC_COMBO | Sí | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Amplía la imagen generada. Puede añadir un costo adicional. (por defecto: "disabled") | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Elimina el fondo de la imagen generada. Puede añadir un costo adicional. (por defecto: false) | BOOLEAN | No | `true`<br>`false` |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. (por defecto: 0) | INT | No | 0 a 2147483647 |

### Entradas del modelo

Compartidas por los modelos `reve-edit@20250915` y `reve-edit-fast@20251030`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model.aspect_ratio` | Relación de aspecto de la imagen de salida. Cuando se establece en `"auto"`, la relación de aspecto se determina automáticamente. (por defecto: "auto") | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Los valores más altos producen mejores imágenes pero cuestan más créditos. (por defecto: 1) | INT | No | 1 a 5 |

### Entradas de ampliación

Se muestra cuando `upscale` se establece en `"enabled"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `upscale.upscale_factor` | Factor de ampliación (2x, 3x o 4x). (por defecto: 2) | INT | No | 2 a 4 |

**Nota:** El parámetro `upscale.upscale_factor` solo aparece cuando `upscale` se establece en `"enabled"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen editada generada según la instrucción. | IMAGE |

**Nota:** Este nodo está marcado como obsoleto.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/es.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
