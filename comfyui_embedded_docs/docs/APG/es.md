> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/es.md)

El nodo APG (Adaptive Projected Guidance) modifica el proceso de muestreo ajustando cómo se aplica la guía durante la difusión. Separa el vector de guía en componentes paralelos y ortogonales en relación con la salida condicional, permitiendo una generación de imágenes más controlada. El nodo proporciona parámetros para escalar la guía, normalizar su magnitud y aplicar momentum para transiciones más suaves entre los pasos de difusión.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Requerido | - | - | El modelo de difusión al que aplicar la guía proyectada adaptativa |
| `eta` | FLOAT | Requerido | 1.0 | -10.0 a 10.0 | Controla la escala del vector de guía paralelo. El comportamiento CFG por defecto se obtiene con un valor de 1. |
| `norm_threshold` | FLOAT | Requerido | 5.0 | 0.0 a 50.0 | Normaliza el vector de guía a este valor, la normalización se desactiva con un valor de 0. |
| `momentum` | FLOAT | Requerido | 0.0 | -5.0 a 1.0 | Controla un promedio móvil de la guía durante la difusión, se desactiva con un valor de 0. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | Devuelve el modelo modificado con la guía proyectada adaptativa aplicada a su proceso de muestreo |