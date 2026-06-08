El nodo ViduExtendVideoNode genera fotogramas adicionales para extender la duración de un video existente. Utiliza un modelo de IA específico para crear una continuación fluida basada en el video de origen y una descripción textual opcional.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la extensión de video. Al seleccionar un modelo, se muestran sus ajustes específicos de duración y resolución. | COMBO | Sí | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `model.duration` | La duración del video extendido en segundos (predeterminado: 4). Este ajuste aparece después de seleccionar un modelo. | INT | Sí | 1 a 7 |
| `model.resolution` | La resolución del video de salida. Este ajuste aparece después de seleccionar un modelo. | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `video` | El video de origen a extender. | VIDEO | Sí | - |
| `prompt` | Una descripción textual opcional para guiar el contenido del video extendido (máximo 2000 caracteres, predeterminado: vacío). | STRING | No | - |
| `semilla` | Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1). | INT | No | 0 a 2147483647 |
| `fotograma_final` | Una imagen opcional para usar como fotograma final objetivo de la extensión. Si se proporciona, su relación de aspecto debe estar entre 1:4 y 4:1, y sus dimensiones deben ser de al menos 128x128 píxeles. | IMAGE | No | - |

**Nota:** El `video` de origen debe tener una duración entre 4 y 55 segundos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video recién generado que contiene el metraje extendido. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
