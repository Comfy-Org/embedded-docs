# EasyCache

El nodo EasyCache implementa un sistema de caché nativo para modelos, mejorando el rendimiento al reutilizar pasos previamente calculados durante el proceso de muestreo. Añade la funcionalidad EasyCache a un modelo con umbrales configurables para cuándo comenzar y detener el uso de la caché durante la línea temporal de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo al que añadir EasyCache. | MODEL | Sí | - |
| `reuse_threshold` | El umbral para reutilizar pasos en caché (predeterminado: 0.2). | FLOAT | Sí | 0.0 - 3.0 |
| `start_percent` | El paso de muestreo relativo para comenzar a usar EasyCache (predeterminado: 0.15). | FLOAT | Sí | 0.0 - 1.0 |
| `end_percent` | El paso de muestreo relativo para finalizar el uso de EasyCache (predeterminado: 0.95). | FLOAT | Sí | 0.0 - 1.0 |
| `verbose` | Si se debe registrar información detallada (predeterminado: False). | BOOLEAN | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model` | El modelo con EasyCache. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/es.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
