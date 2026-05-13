> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/es.md)

Genera videos de forma sincrónica basándose en un prompt de texto e imágenes de inicio/final opcionales. Este nodo utiliza la API de Luma para crear videos, permitiéndote definir el contenido del video mediante un prompt y, opcionalmente, especificar el primer y/o último fotograma para controlar la estructura del video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación del video (predeterminado: "") |
| `model` | COMBO | Sí | Múltiples opciones disponibles | Selecciona el modelo de generación de video entre los modelos Luma disponibles |
| `resolution` | COMBO | Sí | `"540p"`<br>`"720p"<br>`"1080p"`<br>`"4k"` | Resolución de salida para el video generado (predeterminado: "540p"). Este parámetro se ignora al usar el modelo `ray-1-6`. |
| `duration` | COMBO | Sí | `"5s"`<br>`"9s"` | Duración del video generado. Este parámetro se ignora al usar el modelo `ray-1-6`. |
| `loop` | BOOLEAN | Sí | - | Indica si el video generado debe reproducirse en bucle (predeterminado: False) |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (predeterminado: 0) |
| `first_image` | IMAGE | No | - | Primer fotograma del video generado. (opcional) |
| `last_image` | IMAGE | No | - | Último fotograma del video generado. (opcional) |
| `luma_concepts` | CUSTOM | No | - | Conceptos de cámara opcionales para dictar el movimiento de la cámara mediante el nodo Luma Concepts. (opcional) |

**Nota:** Debe proporcionarse al menos uno de los parámetros `first_image` o `last_image`. El nodo generará una excepción si ambos faltan. Los parámetros `resolution` y `duration` se ignoran cuando el `model` está configurado en `ray-1-6`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `210286ad38cecc5b3b0689f470ff473e996abfd251f88a45bcac936751ae2674`
