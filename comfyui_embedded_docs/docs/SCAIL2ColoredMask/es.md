# Crear máscara coloreada SCAIL-2

Este nodo renderiza los datos de seguimiento SAM3 en máscaras coloreadas que son consumidas por el nodo WanSCAILToVideo. Procesa datos de seguimiento de un video de pose de conducción y, opcionalmente, una imagen de referencia, asignando colores consistentes a cada persona rastreada en ambas salidas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `driving_track_data` | Seguimiento SAM3 del video de pose de conducción. Se renderizará en la salida pose_video_mask. | SAM3_TRACK_DATA | Sí | - |
| `ref_track_data` | Seguimiento SAM3 de la(s) imagen(es) de referencia (una identidad por objeto, coloreada en orden de lote), o una MASK simple del sujeto de referencia (renderizada como una sola identidad). | SAM3_TRACK_DATA o MASK | No | - |
| `object_indices` | Lista de índices de personas separados por comas a incluir (ej. '0,2,3'). Se aplica tanto a las máscaras de referencia como a las del video de pose. Vacío = todas. (predeterminado: "") | STRING | Sí | - |
| `sort_by` | Orden en el que se asignan los colores de la paleta a los objetos rastreados (se aplica tanto a la referencia como al video de pose para que cada identidad conserve el mismo color). Los objetos que aparecen en fotogramas anteriores siempre van primero; dentro de un fotograma, left_to_right = el objeto más a la izquierda (por centroide en su primera aparición) recibe el primer color, area = el objeto más grande (por área de máscara en su primera aparición) recibe el primer color; none = mantiene el orden de SAM3. (predeterminado: "left_to_right") | COMBO | Sí | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `replacement_mode` | False = Modo Animación (pose_video_mask tiene fondo negro, reference_image_mask tiene fondo blanco). True = Modo Reemplazo (pose_video_mask tiene fondo blanco, reference_image_mask tiene fondo negro). (predeterminado: False) | BOOLEAN | Sí | False<br>True |

Nota: `object_indices` solo acepta dígitos separados por comas; las entradas no numéricas y los índices fuera de rango se ignoran. Cuando no se proporciona `ref_track_data`, la salida `reference_image_mask` es un relleno sólido usando el color de fondo de referencia (blanco en Modo Animación, negro en Modo Reemplazo).

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `pose_video_mask` | Máscara coloreada renderizada a partir de los datos de seguimiento del video de pose de conducción. El color de fondo sigue la configuración de replacement_mode. | IMAGE |
| `reference_image_mask` | Máscara coloreada renderizada a partir de los datos de seguimiento de la imagen de referencia. El fondo es negro en Modo Reemplazo, blanco en Modo Animación. Si no se proporcionan datos de referencia, devuelve un relleno sólido que coincide con el color de fondo de referencia. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/es.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`
