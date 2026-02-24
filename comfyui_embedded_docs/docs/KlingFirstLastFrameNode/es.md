> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/es.md)

Este nodo utiliza el modelo Kling 3.0 para generar un vídeo. Crea el vídeo basándose en un texto descriptivo, una duración especificada y dos imágenes proporcionadas: un fotograma inicial y un fotograma final. El nodo también puede generar audio para acompañar al vídeo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | La descripción textual que guía la generación del vídeo. Debe tener entre 1 y 2500 caracteres. |
| `duration` | INT | No | 3 a 15 | La duración del vídeo en segundos (valor por defecto: 5). |
| `first_frame` | IMAGE | Sí | N/A | La imagen inicial para el vídeo. Debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. |
| `end_frame` | IMAGE | Sí | N/A | La imagen final para el vídeo. Debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. |
| `generate_audio` | BOOLEAN | No | N/A | Controla si se debe generar audio para el vídeo (valor por defecto: True). |
| `model` | COMBO | No | `"kling-v3"` | Modelo y ajustes de generación. Seleccionar esta opción revela un parámetro anidado `resolution`. |
| `model.resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución para el vídeo generado. Este parámetro solo está disponible cuando `model` está configurado como `"kling-v3"`. |
| `seed` | INT | No | 0 a 2147483647 | Un número utilizado para controlar si el nodo debe volver a ejecutarse. Los resultados son no determinísticos independientemente del valor de `seed` (valor por defecto: 0). |

**Nota:** Las imágenes `first_frame` y `end_frame` deben cumplir con los requisitos de tamaño mínimo y relación de aspecto especificados para que el nodo funcione correctamente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de vídeo generado. |
