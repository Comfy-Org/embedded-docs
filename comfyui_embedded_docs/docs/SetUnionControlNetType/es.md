> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/es.md)

El nodo SetUnionControlNetType permite especificar el tipo de red de control que se utilizará para el condicionamiento. Toma una red de control existente y establece su tipo de control según su selección, creando una copia modificada de la red de control con la configuración de tipo especificada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `control_net` | CONTROL_NET | Sí | - | La red de control a modificar con una nueva configuración de tipo |
| `type` | STRING | Sí | `"auto"`<br>Todas las claves UNION_CONTROLNET_TYPES disponibles | El tipo de red de control a aplicar. Use "auto" para la detección automática de tipo o seleccione un tipo de red de control específico de las opciones disponibles |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `control_net` | CONTROL_NET | La red de control modificada con la configuración de tipo especificada aplicada |

---
**Source fingerprint (SHA-256):** `a64308aec96784f08b6f3f8e96e85f532bd1c536301739e7252b2c7978921b5a`
