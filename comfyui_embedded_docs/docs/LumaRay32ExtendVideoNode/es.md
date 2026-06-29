# LumaRay32ExtendVideoNode

Este nodo extiende una generación de video anterior de Luma Ray 3.2 añadiendo nuevo contenido después (extensión hacia adelante) o antes (extensión hacia atrás). Conecta la salida de ID de generación de un nodo Luma Ray 3.2 anterior para crear una extensión de 5 segundos sin interrupciones de tu video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `source_generation_id` | ID de generación del video Ray 3.2 anterior a extender. Conecta la salida generation_id de otro nodo Luma Ray 3.2. | STRING | Sí | - |
| `direction` | "Forward" continúa después del clip anterior; "backward" se antepone antes de este. Cuando se selecciona "Forward (continue after)", puedes activar opcionalmente el modo de bucle. | COMBO | Sí | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `loop` | Reproduce en bucle el video extendido sin interrupciones (solo extensión hacia adelante). | BOOLEAN | No | True<br>False |
| `prompt` | Texto descriptivo que indica el nuevo contenido a generar. | STRING | Sí | - |
| `resolution` | Resolución de salida para el segmento de video extendido. | COMBO | Sí | "540p"<br>"720p"<br>"1080p" |
| `seed` | Semilla aleatoria para resultados de generación reproducibles. | INT | Sí | - |

**Nota:** El parámetro `loop` solo está disponible cuando `direction` está configurado como "Forward (continue after)". Al usar "Backward (lead-in before)", la opción de bucle no está disponible. El `prompt` debe tener entre 1 y 6000 caracteres.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `generation_id` | El segmento de video extendido generado de 5 segundos. | VIDEO |
| `generation_id` | Identificador único para esta generación, que puede conectarse a otro nodo Luma Ray 3.2 Extend Video para extensiones adicionales. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
