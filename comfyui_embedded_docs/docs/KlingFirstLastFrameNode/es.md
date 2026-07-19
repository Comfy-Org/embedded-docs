# Kling 3.0 Primer-Último Fotograma a Video

Este nodo utiliza el modelo Kling 3.0 para generar un video. Crea el video basándose en un texto descriptivo, una duración especificada y dos imágenes proporcionadas: un fotograma inicial y un fotograma final. El nodo también puede generar audio de acompañamiento para el video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | La descripción textual que guía la generación del video. Debe tener entre 1 y 2500 caracteres. | STRING | Sí | N/A |
| `duración` | La duración del video en segundos (valor predeterminado: 5). | INT | No | 3 a 15 |
| `primer_fotograma` | La imagen inicial del video. Debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. | IMAGE | Sí | N/A |
| `último_fotograma` | La imagen final del video. Debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. | IMAGE | Sí | N/A |
| `generar_audio` | Controla si se genera audio para el video (valor predeterminado: True). | BOOLEAN | No | N/A |
| `modelo` | Configuración del modelo y de generación. Al seleccionar esta opción se muestra un parámetro `resolution` anidado. | COMBO | No | `"kling-v3"` |
| `model.resolution` | La resolución del video generado. Este parámetro solo está disponible cuando el `modelo` está configurado en `"kling-v3"` (valor predeterminado: `"1080p"`). | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `semilla` | Un número utilizado para controlar si el nodo debe reejecutarse. Los resultados no son deterministas independientemente del valor de la semilla (valor predeterminado: 0). | INT | No | 0 a 2147483647 |

**Nota:** Las imágenes `first_frame` y `end_frame` deben cumplir con los requisitos de tamaño mínimo y relación de aspecto especificados para que el nodo funcione correctamente.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
