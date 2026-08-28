# Luma Ray 3.2 Extender Video

Luma Ray 3.2 Extend Video continúa una generación de video anterior de Luma Ray 3.2 creando un nuevo segmento de 5 segundos ya sea después del clip original (hacia adelante) o antes (hacia atrás). Conecte la salida `generation_id` de un nodo Luma Ray 3.2 anterior para usar ese clip como fotograma inicial (hacia adelante) o final (hacia atrás) de la extensión.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `direction` | Forward continúa después del clip anterior; backward se antepone antes de él. Forward usa el clip de origen como fotograma inicial; backward lo usa como fotograma final. Seleccionar "Forward (continue after)" añade la opción `loop`. | DYNAMIC_COMBO | Sí | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `source_generation_id` | ID de generación del video Ray 3.2 anterior que se va a extender. Conecte la salida `generation_id` de otro nodo Luma Ray 3.2. Este valor es obligatorio y no debe estar vacío. | STRING | Sí | – |
| `prompt` | Indicación de texto para el nuevo contenido. Debe tener entre 1 y 6000 caracteres. | STRING | Sí | 1 a 6000 caracteres |
| `resolution` | Resolución de salida para el segmento de video extendido. Predeterminado: "720p". | COMBO | Sí | "540p"<br>"720p"<br>"1080p" |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. Predeterminado: 0. | INT | Sí | 0 a 0xFFFFFFFFFFFFFFFF |

### Entradas de Forward (continue after)

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `loop` | Hacer que el video extendido se repita sin problemas (solo extensión hacia adelante). Predeterminado: False. | BOOLEAN | No | True<br>False |

### Entradas de Backward (lead-in before)

Esta dirección no añade parámetros adicionales.

**Nota:** Las extensiones siempre son de 5 segundos. El parámetro `loop` solo está disponible cuando `direction` es "Forward (continue after)"; cuando se usa "Backward (lead-in before)", la opción `loop` no está disponible. El `prompt` debe tener entre 1 y 6000 caracteres. El `source_generation_id` es obligatorio y debe conectarse desde la salida `generation_id` de un nodo Luma Ray 3.2 anterior.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `VIDEO` | El segmento de video extendido generado de 5 segundos. | VIDEO |
| `generation_id` | Identificador único para esta generación, que puede conectarse a otro nodo Luma Ray 3.2 Extend Video para extensiones adicionales. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
