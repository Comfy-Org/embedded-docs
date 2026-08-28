# PerturbedAttentionGuidance

El nodo PerturbedAttentionGuidance aplica guía de atención perturbada a un modelo de difusión para mejorar la calidad de generación. Ajusta el proceso de eliminación de ruido del modelo durante el muestreo al comparar la predicción condicional normal con una realizada mediante un mecanismo de atención simplificado que solo utiliza proyecciones de valores, y luego agrega la diferencia escalada al resultado. Cuando la escala se establece en 0, el nodo no tiene efecto.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo` | El modelo de difusión al que se le aplica la guía de atención perturbada | MODEL | Sí | - |
| `escala` | La fuerza del efecto de guía de atención perturbada (predeterminado: 3.0). Cuando se establece en 0, el nodo no tiene efecto y devuelve el resultado original de eliminación de ruido. | FLOAT | Sí | 0.0 - 100.0 (paso: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `model` | El modelo modificado con guía de atención perturbada aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/es.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
