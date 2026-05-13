> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/es.md)

El nodo Kling Avatar 2.0 genera videos de humanos digitales estilo transmisión a partir de una sola foto de referencia y un archivo de audio. Crea un video de avatar parlante con un mensaje de texto opcional para definir las acciones, emociones y movimientos de cámara del avatar.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen de referencia del avatar. El ancho y alto deben ser de al menos 300 px. La relación de aspecto debe estar entre 1:2.5 y 2.5:1. |
| `sound_file` | AUDIO | Sí | - | Entrada de audio. Debe tener una duración de entre 2 y 300 segundos. |
| `mode` | COMBO | Sí | `"std"`<br>`"pro"` | El modo de generación a utilizar. |
| `prompt` | STRING | No | - | Mensaje opcional para definir acciones, emociones y movimientos de cámara del avatar. (predeterminado: cadena vacía) |
| `seed` | INT | Sí | 0 a 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) |

**Nota:** Las entradas `image` y `sound_file` tienen requisitos de validación específicos. La imagen debe tener al menos 300x300 píxeles con una relación de aspecto entre 1:2.5 y 2.5:1. El archivo de audio debe tener una duración de entre 2 y 300 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video de humano digital generado. |

---
**Source fingerprint (SHA-256):** `85793d3820a89ef98bb54cb930486847d4fd64cce5470ba34574ec319f8ea8c6`
