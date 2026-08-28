# BriaIncreaseResolution

Bria Increase Resolution amplía una imagen de entrada 2x o 4x mediante el servicio de ampliación de imágenes de Bria, preservando el contenido original. Sube la imagen, la procesa en el servicio de Bria y devuelve el resultado ampliado como imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | La imagen de entrada a ampliar. | IMAGE | Sí | Imagen única |
| `desired_increase` | Multiplicador de resolución. La salida debe tener como máximo 8192 píxeles por lado. | COMBO | Sí | "2"<br>"4" |
| `auto_downscale` | Reduce automáticamente el multiplicador y reduce la escala de la imagen de entrada si eso aún no es suficiente, cuando la salida excedería el límite. (por defecto: False) | BOOLEAN | Sí | True<br>False |
| `moderación` | Configuración de moderación. Cuando se establece en "true", habilita las subopciones `visual_input_moderation` y `visual_output_moderation`, ambas con valor predeterminado False. | DYNAMIC_COMBO | Sí | "false"<br>"true" |

Notas:
- Cuando `moderation` se establece en "true", las subopciones `visual_input_moderation` y `visual_output_moderation` están disponibles, ambas con valor predeterminado False. Controlan la moderación del contenido de la imagen de entrada y de la imagen de salida.
- El nodo aplica un lado máximo de salida de 8192 píxeles. Si el multiplicador seleccionado superara este límite y `auto_downscale` está desactivado, se genera un error. Activar `auto_downscale` permite que el nodo utilice automáticamente un multiplicador menor o reduzca la escala de la imagen de entrada en su lugar.
- Bria primero amplía el lado corto de la imagen de entrada a al menos 224 píxeles antes de ampliarla. Las imágenes demasiado alargadas pueden provocar un error que solicite recortarlas a una forma más cuadrada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La imagen ampliada devuelta por la API de Bria. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/es.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
