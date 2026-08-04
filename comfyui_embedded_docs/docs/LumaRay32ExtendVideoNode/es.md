# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video continúa una generación de video anterior de Luma Ray 3.2 creando un nuevo segmento de 5 segundos, ya sea después del clip original (hacia adelante) o antes de él (hacia atrás). Conecte la salida `generation_id` de un nodo Luma Ray 3.2 anterior para usar ese clip como fotograma inicial (hacia adelante) o final (hacia atrás) de la extensión.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `source_generation_id` | ID de generación del video Ray 3.2 anterior a extender. Conecte la salida `generation_id` de otro nodo Luma Ray 3.2. Este valor es obligatorio y no debe estar vacío. | STRING | Sí | - |
| `direction` | Hacia adelante continúa después del clip anterior; hacia atrás se antepone antes de él. Seleccionar "Forward (continue after)" también agrega la opción `loop`. | COMBO | Sí | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `loop` | Reproduce el video extendido sin interrupciones (solo extensión hacia adelante). Solo disponible cuando `direction` es "Forward (continue after)". Predeterminado: False. | BOOLEAN | No | True<br>False |
| `prompt` | Indicación de texto para el nuevo contenido. Debe tener entre 1 y 6000 caracteres. | STRING | Sí | - |
| `resolution` | Resolución de salida para el segmento de video extendido. Predeterminado: "720p". | COMBO | Sí | "540p"<br>"720p"<br>"1080p" |
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
