> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/es.md)

El nodo ModelSamplingStableCascade aplica un muestreo en cascada estable a un modelo ajustando los parámetros de muestreo con un valor de desplazamiento. Crea una versión modificada del modelo de entrada con una configuración de muestreo personalizada para la generación en cascada estable.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de entrada al que se aplicará el muestreo en cascada estable |
| `shift` | FLOAT | Sí | 0.0 - 100.0 | El valor de desplazamiento a aplicar a los parámetros de muestreo (predeterminado: 2.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con el muestreo en cascada estable aplicado |

---
**Source fingerprint (SHA-256):** `2d0a342fff05434c8fe78999187bd31dbee7deb6f4447759a489102a8ce277de`
