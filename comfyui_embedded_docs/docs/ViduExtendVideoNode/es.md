> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/es.md)

El nodo ViduExtendVideoNode genera fotogramas adicionales para extender la duración de un video existente. Utiliza un modelo de IA específico para crear una continuación fluida basada en el video de origen y una descripción textual opcional.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | COMBO | Sí | `"viduq2-pro"`<br>`"viduq2-turbo"` | El modelo de IA a utilizar para la extensión de video. Al seleccionar un modelo, se muestran sus ajustes específicos de duración y resolución. |
| `model.duration` | INT | Sí | 1 a 7 | La duración del video extendido en segundos (predeterminado: 4). Este ajuste aparece después de seleccionar un modelo. |
| `model.resolution` | COMBO | Sí | `"720p"`<br>`"1080p"` | La resolución del video de salida. Este ajuste aparece después de seleccionar un modelo. |
| `video` | VIDEO | Sí | - | El video de origen a extender. |
| `prompt` | STRING | No | - | Una descripción textual opcional para guiar el contenido del video extendido (máximo 2000 caracteres, predeterminado: vacío). |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1). |
| `end_frame` | IMAGE | No | - | Una imagen opcional para usar como fotograma final objetivo de la extensión. Si se proporciona, su relación de aspecto debe estar entre 1:4 y 4:1, y sus dimensiones deben ser de al menos 128x128 píxeles. |

**Nota:** El `video` de origen debe tener una duración entre 4 y 55 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video recién generado que contiene el metraje extendido. |

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
