# Luma Image to Video

Genera videos de forma sincrónica basándose en un prompt de texto e imágenes de inicio/final opcionales. Este nodo utiliza la API de Luma para crear videos, permitiéndote definir el contenido del video mediante un prompt y, opcionalmente, especificar el primer y/o último fotograma para controlar la estructura del video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para la generación del video (predeterminado: "") | STRING | Sí | - |
| `model` | Selecciona el modelo de generación de video entre los modelos Luma disponibles | COMBO | Sí | Múltiples opciones disponibles |
| `resolución` | Resolución de salida para el video generado (predeterminado: "540p"). Este parámetro se ignora al usar el modelo `ray-1-6`. | COMBO | Sí | `"540p"`<br>`"720p"<br>`"1080p"`<br>`"4k"` |
| `duración` | Duración del video generado. Este parámetro se ignora al usar el modelo `ray-1-6`. | COMBO | Sí | `"5s"`<br>`"9s"` |
| `bucle` | Indica si el video generado debe reproducirse en bucle (predeterminado: False) | BOOLEAN | Sí | - |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 18446744073709551615 |
| `primera_imagen` | Primer fotograma del video generado. (opcional) | IMAGE | No | - |
| `última_imagen` | Último fotograma del video generado. (opcional) | IMAGE | No | - |
| `luma_concepts` | Conceptos de cámara opcionales para dictar el movimiento de la cámara mediante el nodo Luma Concepts. (opcional) | CUSTOM | No | - |

**Nota:** Debe proporcionarse al menos uno de los parámetros `first_image` o `last_image`. El nodo generará una excepción si ambos faltan. Los parámetros `resolution` y `duration` se ignoran cuando el `model` está configurado en `ray-1-6`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `210286ad38cecc5b3b0689f470ff473e996abfd251f88a45bcac936751ae2674`
