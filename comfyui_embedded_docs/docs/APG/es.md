# Guía Adaptativa Proyectada

El nodo APG (Adaptive Projected Guidance) modifica el proceso de muestreo ajustando cómo se aplica la guía durante la difusión. Separa el vector de guía en componentes paralela y ortogonal con respecto a la salida condicional, lo que permite una generación de imágenes más controlada. El nodo proporciona parámetros para escalar la guía, normalizar su magnitud y aplicar impulso para transiciones más suaves entre los pasos de difusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplica la guía adaptativa proyectada | MODEL | Sí | - |
| `eta` | Controla la escala del vector de guía paralelo. Comportamiento CFG predeterminado con un valor de 1 (predeterminado: 1.0). | FLOAT | Sí | -10.0 a 10.0 |
| `norm_threshold` | Normaliza el vector de guía a este valor; la normalización se desactiva con un valor de 0 (predeterminado: 5.0). | FLOAT | Sí | 0.0 a 50.0 |
| `momentum` | Controla un promedio móvil de la guía durante la difusión; se desactiva con un valor de 0 (predeterminado: 0.0). | FLOAT | Sí | -5.0 a 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | Devuelve el modelo modificado con la guía adaptativa proyectada aplicada a su proceso de muestreo | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/es.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
