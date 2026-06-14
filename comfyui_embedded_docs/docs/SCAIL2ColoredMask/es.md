# SCAIL2ColoredMask

Este nodo convierte los datos de seguimiento de SAM3 en máscaras de colores que son consumidas por el nodo WanSCAILToVideo. Procesa los datos de seguimiento de un video de pose guía y opcionalmente una imagen de referencia, asignando colores consistentes a cada persona rastreada en ambas salidas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `driving_track_data` | Seguimiento SAM3 del video de pose guía. Se renderizará en la salida pose_video_mask. | SAM3_TRACK_DATA | Sí | - |
| `ref_track_data` | Seguimiento SAM3 de la imagen de referencia. | SAM3_TRACK_DATA | No | - |
| `object_indices` | Lista separada por comas de índices de personas a incluir (ej. '0,2,3'). Se aplica tanto a la máscara de referencia como a la del video de pose. Vacío = todas. | STRING | Sí | - |
| `sort_by` | Orden en que se asignan los colores de la paleta a los objetos rastreados (se aplica tanto a la referencia como al video de pose para que cada identidad mantenga el mismo color). left_to_right = el objeto más a la izquierda (por centroide del primer fotograma) recibe el primer color; area = el objeto más grande (por área de máscara del primer fotograma) recibe el primer color; none = mantener el orden de SAM3. (predeterminado: "left_to_right") | COMBO | Sí | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `replacement_mode` | False = Modo Animación (pose_video_mask tiene fondo negro, reference_image_mask tiene fondo blanco). True = Modo Reemplazo (pose_video_mask tiene fondo blanco, reference_image_mask tiene fondo negro). (predeterminado: False) | BOOLEAN | Sí | False<br>True |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `pose_video_mask` | Máscara de colores renderizada a partir de los datos de seguimiento del video de pose guía. El color de fondo sigue la configuración de replacement_mode. | IMAGE |
| `reference_image_mask` | Máscara de colores renderizada a partir de los datos de seguimiento de la imagen de referencia. Siempre se renderiza con fondo negro según la convención del modelo. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/es.md)

---
**Source fingerprint (SHA-256):** `c9f6d87410b8bd4082ffb06ef1cf973829566ed222be643db3528cbc241d3c14`
