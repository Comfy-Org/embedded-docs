# DesactivarRuido

El nodo `DisableNoise` proporciona una configuración de ruido vacía que puede utilizarse para desactivar la generación de ruido en los procesos de muestreo. Devuelve un objeto de ruido especial que no contiene datos de ruido, lo que permite que otros nodos omitan operaciones relacionadas con el ruido cuando se conectan a esta salida. El nodo también se puede buscar bajo el alias "zero noise".

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| *No requiere parámetros de entrada* | Este nodo no requiere ningún parámetro de entrada. | - | - | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `NOISE` | Devuelve una configuración de ruido vacía que puede utilizarse para desactivar la generación de ruido en los procesos de muestreo. | NOISE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/es.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
