# PerturbedAttentionGuidance

El nodo PerturbedAttentionGuidance aplica guía de atención perturbada a un modelo de difusión para mejorar la calidad de generación. Modifica el mecanismo de autoatención del modelo durante el muestreo reemplazándolo por una versión simplificada que se centra en las proyecciones de valores. Esta técnica ayuda a mejorar la coherencia y la calidad de las imágenes generadas al ajustar el proceso de eliminación de ruido condicional.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplica la guía de atención perturbada | MODEL | Sí | - |
| `scale` | La fuerza del efecto de guía de atención perturbada (predeterminado: 3.0). Cuando se establece en 0, el nodo no tiene efecto y devuelve el resultado original sin ruido. | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con guía de atención perturbada aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/es.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
