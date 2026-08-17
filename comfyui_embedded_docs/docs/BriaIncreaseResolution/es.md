# BriaIncreaseResolution

Bria Increase Resolution amplía una imagen de entrada por 2x o 4x utilizando la API de ampliación de imágenes de Bria, preservando el contenido original. Sube la imagen, la procesa en el servicio de Bria y devuelve el resultado ampliado como imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La imagen de entrada para ampliar. | IMAGE | Sí | Imagen única |
| `desired_increase` | Multiplicador de resolución. La salida debe caber dentro de 8192 píxeles en cada lado. | COMBO | Sí | "2"<br>"4" |
| `auto_downscale` | Reduce automáticamente el multiplicador y reduce la escala de la imagen de entrada si aún no es suficiente, cuando la salida excedería el límite. (valor predeterminado: False) | BOOLEAN | Sí | True<br>False |
| `moderation` | Configuración de moderación. Cuando se establece en "true", habilita las subopciones `visual_input_moderation` y `visual_output_moderation`, ambas con valor predeterminado False. | DYNAMIC_COMBO | Sí | "false"<br>"true" |

Notas:
- El nodo aplica un máximo de 8192 píxeles por lado en la salida. Si el multiplicador seleccionado excede este límite y `auto_downscale` está deshabilitado, se genera un error. Habilitar `auto_downscale` permite que el nodo use automáticamente un multiplicador menor o reduzca la escala de la imagen de entrada.
- Bria primero amplía el lado corto de la imagen de entrada a al menos 224 píxeles antes de aumentar la resolución. Las imágenes demasiado alargadas pueden provocar un error que pide recortarlas para que tengan una forma más cuadrada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La imagen ampliada devuelta por la API de Bria. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/es.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
