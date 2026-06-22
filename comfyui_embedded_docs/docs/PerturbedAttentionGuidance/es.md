# PerturbedAttentionGuidance

El nodo PerturbedAttentionGuidance aplica guía de atención perturbada a un modelo de difusión para mejorar la calidad de generación. Modifica el mecanismo de autoatención del modelo durante el muestreo, reemplazándolo con una versión simplificada que se centra en las proyecciones de valores. Esta técnica ayuda a mejorar la coherencia y calidad de las imágenes generadas ajustando el proceso de eliminación de ruido condicional.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se aplicará la guía de atención perturbada | MODEL | Sí | - |
| `escala` | La intensidad del efecto de guía de atención perturbada (predeterminado: 3.0). Cuando se establece en 0, el nodo no tiene efecto y devuelve el resultado original de eliminación de ruido. | FLOAT | No | 0.0 - 100.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con guía de atención perturbada aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/es.md)

---
**Source fingerprint (SHA-256):** `8808aa3a3f7cfe306e17f8f4424779cb8e4565647bbcc9d4907da2215affe191`
