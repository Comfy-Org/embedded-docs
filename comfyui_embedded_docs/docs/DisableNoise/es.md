> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/es.md)

El nodo `DisableNoise` proporciona una configuración de ruido vacía que puede utilizarse para desactivar la generación de ruido en procesos de muestreo. Devuelve un objeto de ruido especial que no contiene datos de ruido, permitiendo que otros nodos omitan operaciones relacionadas con el ruido cuando se conectan a esta salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| *Sin parámetros de entrada* | - | - | - | Este nodo no requiere ningún parámetro de entrada. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `NOISE` | NOISE | Devuelve una configuración de ruido vacía que puede utilizarse para desactivar la generación de ruido en procesos de muestreo. |

---
**Source fingerprint (SHA-256):** `527152dff69bd5c55c622c634b87e625eb16708f8595fa02d69cf38f1125c5eb`
